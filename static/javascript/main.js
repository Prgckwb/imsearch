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

function isEmpty(obj) {
    return !Object.keys(obj).length;
}

// クエリ情報を吐き出す
function activateFeatureOption() {
    let queries = getUrlQueries()
    if (isEmpty(queries)) {
        let default_feature = document.getElementById("10")
        default_feature.classList.add("is-active")
    } else {
        let feature_option = document.getElementById(query_f)
        feature_option.classList.add("is-active")
    }

}