HEADER = '''
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="static/css/styles.css">
    <link rel="script" href="static/javascript/main.js">
    <title>柳井研究室CGI課題</title>
</head>
'''


def get_page(image, feature):
    html_text = f'''
    <!DOCTYPE html>
    <html lang="ja">
    {HEADER}
    <body>
    <section class="section">
        <div class="container">
            <p class="title is-2 has-text-centered">
                Image Search by {feature} with Histogram Intersection {image}
            </p>
    
            <div class="columns">
                <div class="column">
                    <div class="block">
                        <p class="title is-4">Query Image</p>
                        <img src="{image}" alt="">
                    </div>
                    
                    <!-- 特徴量切り替え -->
                    <div class="feature-options menu">
                        <p class="title is-4">Feature Options</p>
                        
                        <div class="intersec-option">
                            <p class="menu-label">Intersection</p>
                            <ul class="menu-list">
                                <li><a href="?image={image}&feature=0">RGB Color Histogram 1×1</a></li>
                                <li><a href="?image={image}&feature=1">RGB Color Histogram 2×2</a></li>
                                <li><a href="?image={image}&feature=2">RGB Color Histogram 3×3</a></li>
                            </ul>
                        </div>
                    </div>
                </div>        
            </div>
        </div>
    </section>
    </body>
    </html>
    '''
    return html_text
