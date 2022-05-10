function getUrlQueries() {
    let queryStr = window.location.search.slice(1);
    let queries = {};

    if (!queryStr) {
        return queries
    }

    queryStr.split('&').forEach(function (queryStr) {
        let queryArr = queryStr.split('=');
        queries[queryArr[0]] = queryArr[1];
    });

    return queries
}

function activateFeatureOption() {
    let queries = getUrlQueries()
    console.log(queries)
}