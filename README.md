
Simple browser-based plots, generated from python, using the latest libraries:

* [Dash: Reactive Web Apps for python](https://github.com/plotly/dash)
* [Bokeh: Interactive Web Plotting for Python](https://github.com/bokeh/bokeh)

## Dash
### Run

Start the server, running at [localhost:8050](http://localhost:8050/)

```
docker build -t dash-app -f Dockerfile-Dash .
docker run -it --rm --name=plotly-dash -p 127.0.0.1:8050:8050 dash-app
```

![capture](https://user-images.githubusercontent.com/4110571/28351239-2a56e580-6c14-11e7-8101-04c6e5de030e.gif)

## Bokeh
### Run

Start the server, running at [localhost:5000](http://localhost:5000/)
```
docker build -t bokeh-app -f Dockerfile-Bokeh .
docker run -it --rm --name=bokeh-flask -p 127.0.0.1:5000:5000 bokeh-app
```

![capture](https://user-images.githubusercontent.com/4110571/28354482-a42396f4-6c25-11e7-8bc9-c03be132b6b5.gif)

