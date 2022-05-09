# HTML情報を返す
def get_page(image, feature, images_list):
    head_text = create_head()
    images_table = create_images_table(image, feature, images_list)
    feature_options = create_feature_options(image)

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
            
            <p class="title is-3 has-text-centered">
                [DEBUG] Query: f = {feature}, i = {image}
            </p>
            
            <div class="columns">
            
                <!-- クエリ画像と特徴抽出手法選択-->
                <div class="column is-one-fifth">
                    <div class="block">
                        <p class="title is-4">Query Image</p>
                        <img src="{images_list[int(image)]}" alt=""
                        style="width: 250px; height: 200px; object-fit: cover">
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
def create_images_table(image, feature, images_list):
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
            # 画像テーブルの列に対して画像をtable_wの分作成
            # language=HTML
            images_table += f'''
               <td><a href="./?i={table_w * i + j}&f={feature}">
                   <img src="{images_list[table_w * i + j]}" alt="hoge" 
                   style="width: {image_w}px; height:{image_h}px; object-fit: cover">
               </a></td>
           '''

        # language=HTML
        images_table += "</tr>"
    return images_table


# 特緒量選択リストを作成する
def create_feature_options(image):
    # language=HTML
    feature_options = f'''
    <div class="feature-options menu">
        <p class="title is-4">Feature Options</p>

        <div class="intersec-option">
            <p class="menu-label">Intersection</p>
            <ul class="menu-list">
                <li><a href="?i={image}&f=0">RGB Color Histogram 1×1</a></li>
                <li><a href="?i={image}&f=1">RGB Color Histogram 2×2</a></li>
                <li><a href="?i={image}&f=2">RGB Color Histogram 3×3</a></li>

                <li><a href="?i={image}&f=3">HSV Color Histogram 1×1</a></li>
                <li><a href="?i={image}&f=4">HSV Color Histogram 2×2</a></li>
                <li><a href="?i={image}&f=5">HSV Color Histogram 3×3</a></li>

                <li><a href="?i={image}&f=6">LUV Color Histogram 1×1</a></li>
                <li><a href="?i={image}&f=7">LUV Color Histogram 2×2</a></li>
                <li><a href="?i={image}&f=8">LUV Color Histogram 3×3</a></li>
            </ul>
        </div>
    </div>
    '''
    return feature_options
