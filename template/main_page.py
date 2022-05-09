from util import FEATURES_NAME_EUCLID, FEATURES_NAME_INTERSEC


# HTML情報を返す
def get_page(query_index, feature, images_list, sorted_list):
    head_text = create_head()
    images_table = create_images_table(feature, sorted_list)
    feature_options = create_feature_options(query_index)

    # language=HTML
    html_text = f'''
    <!DOCTYPE html>
    <html lang="ja">
   {head_text}
    <body>
    
    <section class="section">
        <div class="container">
        
            <!-- タイトル -->
            <p class="title is-2 has-text-centered">
                Image Search by ??? with ???
            </p>
            
            <p class="title is-3 has-text-centered has-text-danger">
                [DEBUG] Query: f = {feature}, i = {query_index}
            </p>
            
            <div class="columns">
            
                <!-- クエリ画像と特徴抽出手法選択-->
                <div class="column is-one-fifth">
                    <div class="block">
                        <p class="title is-4">Query Image</p>
                        <img src="{images_list[query_index].path}" alt=""
                        style="width: 250px; height: 200px; object-fit: cover">
                        <p class="has-text-danger">{images_list[query_index]}</p>
                    </div>

                    <!-- 特徴量切り替え -->
                    {feature_options}
                </div>

                <!-- 画像のテーブル-->
                <div class="image-tables column">
                    <p class="title is-4">Similar Images</p>
                    <table class="table is-bordered">
                        <tr>{images_table}</tr>
                    </table>
                </div>
            </div>
        </div>
    </section>
    </body>
    </html>
    '''
    return html_text


# HTMLのheadタグ情報を作成
def create_head():
    # language=HTML
    head_text = f'''
     <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="static/css/styles.css">
        <link rel="script" href="static/javascript/main.js">
        <title>柳井研究室CGI課題</title>
    </head>
    '''
    return head_text


# 画像一覧テーブルを作成する
def create_images_table(feature, images_list):
    # 画像テーブルのサイズ
    table_w = 7
    table_h = 10

    # 画像のサイズ
    image_w = 200
    image_h = 100

    images_table = ""

    for i in range(table_h):

        # 画像テーブルの列を作成
        # language=HTML
        images_table += "<tr>"

        for j in range(table_w):
            n = table_w * i + j
            # 画像テーブルの列に対して画像をtable_wの数 作成
            # language=HTML
            images_table += f'''
               <td>
                   <a href="./?i={images_list[n].index}&f={feature}">
                       <img src="{images_list[n].path}" alt="hoge" 
                       style="width: {image_w}px; height:{image_h}px; object-fit: cover">
                   </a><br>
                   <p class="is-text has-text-centered">
                        [{images_list[n].index}] {images_list[n].similarity:.4f}
                   </p>
               </td>
           '''

        # language=HTML
        images_table += "</tr>"
    return images_table


# 特緒量選択リストを作成する
def create_feature_options(image):
    # language=HTML
    feature_options = f'''
    <div class="content">
        <div class="feature-options menu">
        <p class="title is-4">Feature Options</p>
    '''

    # language=HTML
    feature_options += f'''
        <div class="intersec-option">
            <p class="menu-label">Intersection</p>
            <ul class="menu-list">
    '''
    for key, value in FEATURES_NAME_INTERSEC.items():
        # language=HTML
        feature_options += f'''
            <li><a href="?i={image}&f={key}">{value}</a></li>
        '''

        # <li><a href="?i={image}&f=1">RGB Color Histogram 2×2</a></li>
        # <li><a href="?i={image}&f=2">RGB Color Histogram 3×3</a></li>
        #
        # <li><a href="?i={image}&f=3">HSV Color Histogram 1×1</a></li>
        # <li><a href="?i={image}&f=4">HSV Color Histogram 2×2</a></li>
        # <li><a href="?i={image}&f=5">HSV Color Histogram 3×3</a></li>
        #
        # <li><a href="?i={image}&f=6">LUV Color Histogram 1×1</a></li>
        # <li><a href="?i={image}&f=7">LUV Color Histogram 2×2</a></li>
        # <li><a href="?i={image}&f=8">LUV Color Histogram 3×3</a></li>
        #
        # <li><a href="?i={image}&f=9">DCNN Features</a> </li>
    # language=HTML
    feature_options += f''' 
    </ul></div>
    <div class="euclid-option">
    <p class="menu-label">Euclid</p>
    <ul class="menu-list">
    '''
    for key, value in FEATURES_NAME_EUCLID.items():
        # language=HTML
        feature_options += f'''
            <li><a href="?i={image}&f={key}">{value}</a></li>
        '''
        feature_options += "</ul></div></div>"
        # <li></li>
        # <li><a href="?i={image}&f=11">RGB Color Histogram 2×2</a></li>
        # <li><a href="?i={image}&f=12">RGB Color Histogram 3×3</a></li>
        #
        # <li><a href="?i={image}&f=13">HSV Color Histogram 1×1</a></li>
        # <li><a href="?i={image}&f=14">HSV Color Histogram 2×2</a></li>
        # <li><a href="?i={image}&f=15">HSV Color Histogram 3×3</a></li>
        #
        # <li><a href="?i={image}&f=16">LUV Color Histogram 1×1</a></li>
        # <li><a href="?i={image}&f=17">LUV Color Histogram 2×2</a></li>
        # <li><a href="?i={image}&f=18">LUV Color Histogram 3×3</a></li>
        #
        # <li><a href="?i={image}&f=19">DCNN Features</a> </li>

    return feature_options
