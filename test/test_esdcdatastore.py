from unittest import TestCase

from cate.core.ds import DATA_STORE_REGISTRY


class EsdcDataStoreTest(TestCase):
    def test_plugin_called(self):
        data_store = DATA_STORE_REGISTRY.get_data_store('esdc')
        self.assertIsNotNone(data_store)
        self.assertEqual(data_store.id, 'esdc')
        self.assertEqual(data_store.title, 'Earth System Data Cube')


