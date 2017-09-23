import warnings
from typing import Optional, Any, Sequence

import cablab
from cate.conf import conf
from cate.core import DataStore, DataSource
from cate.core.ds import DATA_STORE_REGISTRY
from cate.core.types import TimeRangeLike, PolygonLike, VarNamesLike
from cate.util import Monitor, OrderedDict


class EsdcDataSource(DataSource):
    def __init__(self, data_store: 'EsdcDataStore', ds_id: str, title: str, cube: cablab.Cube):
        self._data_store = data_store
        self._ds_id = ds_id
        self._title = title
        self._cube = cube

    @property
    def data_store(self) -> 'EsdcDataStore':
        return self._data_store

    @property
    def id(self) -> str:
        return self._ds_id

    @property
    def meta_info(self) -> Optional[dict]:
        metadata = dict()
        for key, value in self._cube.config.__dict__.items():
            if not key.startswith('_') and not key.endswith('_'):
                metadata[key] = str(value)
        if self._title:
            metadata['title'] = self._title
        return metadata

    def open_dataset(self,
                     time_range: TimeRangeLike.TYPE = None,
                     region: PolygonLike.TYPE = None,
                     var_names: VarNamesLike.TYPE = None,
                     protocol: str = None) -> Any:
        if time_range or region or var_names:
            raise ValueError("ESDCdata source cannot have constraints")
        return self._cube.data.dataset()

    def make_local(self, *args, **kwargs) -> Optional['DataSource']:
        warnings.warn('EsdcDataSource cannot be made local')
        return None

    def _repr_html_(self):
        # TODO (forman): implement me
        return self.__repr__()


class EsdcDataStore(DataStore):
    def __init__(self):
        super().__init__('esdc', title='Earth System Data Cube')
        esdc_data_source_defs = conf.get_config_value('esdc_data_sources', [])
        self._data_sources = OrderedDict()
        for ds_id, title, local_path in esdc_data_source_defs:
            if ds_id.startswith('esdc.'):
                ds_id = 'esdc.' + ds_id
            cube = None
            try:
                cube = cablab.Cube.open(local_path)
            except Exception as e:
                warnings.warn('ESDC data source "%s" registered: %s' % (ds_id, e))
                pass
            if cube:
                self._data_sources[ds_id] = EsdcDataSource(self, ds_id, title, cube)

    def query(self,
              id: str = None,
              query_expr: str = None,
              monitor: Monitor = Monitor.NONE) -> Sequence[DataSource]:
        if id:
            return self._data_sources.get(id)
        # TODO (forman): use query_expr
        return list(self._data_sources.values())

    def _repr_html_(self):
        # TODO (forman): implement me
        return self.__repr__()


def cate_init():
    DATA_STORE_REGISTRY.add_data_store(EsdcDataStore())
