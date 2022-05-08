def get_page(image, feature):
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
                <div class="column">
                    <form action="index.cgi" method="post">
                        <input type="text" class="input" name="image"> 
                        値を入力してください
                        <input type="submit" class="button is-primary" name="submit" value="送信">
                    </form>
                </div>        
            </div>
        </div>
    </section>
    </body>
    </html>
    '''
    return html_text
