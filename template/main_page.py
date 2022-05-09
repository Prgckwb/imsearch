import glob


def get_page(image, feature):

    table_w = 7
    table_h = 10
    images_table = ""
    imgs = [img for img in glob.glob("static/images/ramen/*.jpg")]

    for i in range(table_h):
        # language=HTML
        images_table += "<tr>"
        for j in range(table_w):
            # language=HTML
            images_table += f'''
                    <td><a href="./?image={7*i+j}&feature={feature}">
                        <img src={imgs[7*i+j]} alt="hoge" style="width: 120px; height:90px; object-fit: cover">
                    </a></td>
                    '''
        # language=HTML
        images_table += "</tr>"

    # language=HTML
    html_text = f'''
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="static/css/styles.css">
        <link rel="script" href="static/javascript/main.js">
        <title>柳井研究室CGI課題</title>
    </head>
    <body>
    <section class="section">
        <div class="container">
            <p class="title is-2 has-text-centered">
                Image Search by {feature} with Histogram Intersection {image}
            </p>
            
            <div class="columns">
                <div class="column is-one-fifth">
                    <div class="block">
                        <p class="title is-4">Query Image</p>
                        <img src="static/images/ramen/2192.jpg" alt="" class="image is-128x128">
                    </div>

                    <!-- 特徴量切り替え -->
                    <div class="feature-options menu">
                        <p class="title is-4">Feature Options</p>

                        <div class="intersec-option">
                            <p class="menu-label">Intersection</p>
                            <ul class="menu-list">
                                <li><a href="?image={image}&feature=rgb1i">RGB Color Histogram 1×1</a></li>
                                <li><a href="?image={image}&feature=rgb2i">RGB Color Histogram 2×2</a></li>
                                <li><a href="?image={image}&feature=rgb3i">RGB Color Histogram 3×3</a></li>

                                <li><a href="?image={image}&feature=hsv1i">HSV Color Histogram 1×1</a></li>
                                <li><a href="?image={image}&feature=hsv2i">HSV Color Histogram 2×2</a></li>
                                <li><a href="?image={image}&feature=hsv3i">HSV Color Histogram 3×3</a></li>

                                <li><a href="?image={image}&feature=luv1i">LUV Color Histogram 1×1</a></li>
                                <li><a href="?image={image}&feature=luv2i">LUV Color Histogram 2×2</a></li>
                                <li><a href="?image={image}&feature=luv3i">LUV Color Histogram 3×3</a></li>
                            </ul>
                        </div>
                    </div>
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
