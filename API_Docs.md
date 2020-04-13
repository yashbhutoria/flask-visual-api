# Note
APIs returns png image as a base64 string

# Available APIs
## 1. BarGraph

#### Endpoint
```
POST /graph
```

#### Sample Payload
```json
{
    "metadata": {
        "X": "XLabel",
        "Y": "YLabel"
    },
    "data": [{
            "X": "Foo1",
            "Y": 10
        },
        {
            "X": "Foo2",
            "Y": 5
        }
    ]
}
```
#### Resulting Image
![BarGraph](/samples/graph.png)

## 2. LinePlot
plots bar graph for the given data
#### Endpoint
```
POST /lineplot
```
#### Sample Payload
```json
{
    "metadata": {
        "X": "XLabel",
        "Y": "YLabel"
    },
    "data": {
        "line1": {
            "Foo1": 1.0528454438253931,
            "Foo2": 1.1216946408721025,
            "Foo3": 1.0112659123311298
        },
        "line2": {
            "Foo1": 2.0528454438253931,
            "Foo2": 2.1216946408721025,
            "Foo3": 2.0112659123311298
        }
    }
}
```
#### Resulting Image
![BarGraph](/samples/lineplot.png)

## 3. MultiBar Plot
plots bar graph for the given data
#### Endpoint
```
POST /multibar
```
#### Sample Payload
```json
{
    "metadata": {
        "X": "XLabel",
        "Y": "YLabel"
    },
    "data": {
        "line1": {
            "Foo1": 1.0528454438253931,
            "Foo2": 1.1216946408721025,
            "Foo3": 1.0112659123311298
        },
        "line2": {
            "Foo1": 2.0528454438253931,
            "Foo2": 2.1216946408721025,
            "Foo3": 2.0112659123311298
        }
    }
}
```
#### Resulting Image
![BarGraph](/samples/multibar.png)

## 4. Scatter Plot
plots scatter plot for the given data
#### Endpoint
```
POST /scatter
```
#### Sample Payload
```json
{
    "metadata": {
        "X": "XLabel",
        "Y": "YLabel"
    },
    "data": [
        {
            "x": 12,
            "y": 23
        },
        {
            "x": 14,
            "y": 33
        },
        {
            "x": 16,
            "y": 43
        },
        {
            "x": 18,
            "y": 30
        },
        {
            "x": 20,
            "y": 40
        }
    ]
}
```
#### Resulting Image
![ScatterPlot](/samples/scatter.png)


## 4. Funnel Plot
plots funnel plot for the given data
#### Endpoint
```
POST /funnel
```
#### Sample Payload
```json
{
    "metadata": {
        "X": "XLable",
        "Y": "YLable"
    },
    "data": [
        {
            "segment": "Segment 2",
            "value": 2
        },
        {
            "segment": "Segment 1",
            "value": 1
        },
        {
            "segment": "Segment 3",
            "value": 3
        }
    ]
}
```
#### Resulting Image
![Funnel Plot](samples/funnel_plot.png)