# hexo-jupyter-notebook

Use jupyter notebook like *.ipynb in Hexo.

## Installation


``` bash
$ npm install hexo-jupyter-notebook --save
```

## Usage
Check if pandoc is installed (pandoc --version); if needed, install:
``` bash
sudo apt-get install pandoc
``` 
Or mac
``` bash
brew install pandoc
```

make sure the python you use have isntalled `nbconvert`, if not , use 

``` bash
pip install nbconvert
```

1. Enable post asset by adding this line in your `_config.yml`: `post_asset_folder: true`
2. put your jupyter file in post asset directory. You can use `ln -s` , `cp source direction` and etc. 
3. Make sure load jquery 2 (jquery 3 will error. I will fix at soon.) before you use `asset_jupyter`

``` html
<script text='text/javascript' src='/path/to/jquery.js'></script>
{% asset_jupyter python_path jupyter_file_name %}


eg : (i use next theme , so the jquery is in lib/jquery/index.js)
<script text='text/javascript' src='/lib/jquery/index.js'></script>
{% asset_jupyter /data1/anaconda3/bin/python crash-mxnet-ndarray.ipynb %}

```

## future
Maybe it's a little diffcult to use.. But it's work. You can see example at [my blog](http://blog.qiliuxiansheng.com)

1. The jupyter notebook width is fixed for general usage. Maybe it should be auto-responsive.
2. This assums that you must use post_asset_folder. I think it's a good choice for you to manage your blog and notebook files. For linux and mac user, you are encouraged to use `ln -s ` command to link you jupyter notebook file to blog. 


## License

MIT
