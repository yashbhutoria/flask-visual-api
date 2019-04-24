# flask-visual-api
A number of APIs hosted on a flask server that returns visualisations.
The visulaisations

# Available APIs
## 1. BarGraph

#### Endpoint
```
/graph
```

plots bar graph for the given schema

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

## 2. LinePlot
plots bar graph for the given schema
#### Endpoint
```
/lineplot
```

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
## 3. MultiBar Plot
plots bar graph for the given schema
#### Endpoint
```
/multibar
```

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