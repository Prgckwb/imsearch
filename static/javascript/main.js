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

// クエリ情報を吐き出す
function activateFeatureOption() {
    let queries = getUrlQueries()
    let feature_option = document.getElementById(queries['f'])
    feature_option.classList.add("is_active")
}