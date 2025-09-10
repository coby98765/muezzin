# muezzin/API
a public gateway to the data reports, 
including a path the get all reports, 
a path to get all reports that `is_bds` = True, 
a path to get all reports by `theret_level`, 
a path to search report transcripts content.
## ENV
```commandline
ES_HOST
API_PORT
```
## Paths
- `GET` : `/all`
- `GET` : `/is_bds`
- `GET` : `/theret_level/<level>`
- `GET` : `/search?query=`


## Libraries
`elasticsearch`,`logging`.
