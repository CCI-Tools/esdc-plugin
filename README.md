# esdc-plugin

Cate plugin adding a data store for Earth System Data Cube (ESDC) instances


## Installation


Create a Cate environment by using the Cate installer call **Cate CLI** to open a shell
with activated Python environment.
Alternatively, create the environment from [cate](https://github.com/CCI-Tools/cate-core) sources:

    git clone https://github.com/CCI-Tools/cate-core.git
    cd cate-core
    conda env create
    activate cate
    python setup.py develop


Install [cablab](https://github.com/CAB-LAB/cablab-core):

    cd ..
    git clone https://github.com/CAB-LAB/cablab-core.git
    cd cablab-core
    python setup.py develop

Install [esdc-plugin](https://github.com/CCI-Tools/esdc-plugin)

    cd ..
    git clone https://github.com/CCI-Tools/esdc-plugin.git
    cd esdc-plugin
    python setup.py develop

Test installation of plugin

    cate -h
    python -c "import cate"


## Configuration

In `$HOME/.cate/conf.py` define a list named `esdc_data_sources`. Its entries are tuples of the form
`(<id>, <title>, <path>)`, where

* `id` - arbitrary identifier, must be a non-empty string
* `title` - arbitrary title
* `path` - local path to your ESDC

For example:

    esdc_data_sources = [
        ('esdc.lr_cube', 'ESDC 0.5 degrees, v1.0', '/home/hans/data/esdc/cube-lr-1.0'),
        ('esdc.hr_cube', 'ESDC 0.025 degrees, v1.1', '/home/hans/data/esdc/cube-hr-1.1'),
    ]


