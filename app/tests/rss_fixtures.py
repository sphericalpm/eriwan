rv_xml = '''<?xml version='
    1.0' encoding='UTF-8'?><rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">< channel >< title > Eriwan_Podcast < / title >< link > 127.0.0.1
     < / link >
    < description > Eriwan_Podcast < / description >
    < itunes:explicit > yes < / itunes:explicit >
    < docs > http: // www.rssboard.org / rss-specification < / docs >
    < generator > python-podgen v1.0.0 https: // podgen.readthedocs.org < / generator >
    < lastBuildDate > Sun, 18 Aug 2019 09:56:28 +0000 < / lastBuildDate >
    < item >< title > NAME EPS < / title >< link > 127.0.0.1 < / link >< itunes:author > & lt;User John & gt; < / itunes:author >< author >21124 @ mail.ru( & lt;User John & gt;)</author><guidisPermaLink="false">127.0.0.1</guid ><enclosureurl = "127.0.0.1"length="454599964"type="mp3"/>< / item ></channel></rss >'''
rv_html = '''
    <!-- HERE WILL BE MAIN PAGE-->
<!DOCTYPE html>
<html>
  <head>
    <title>
Eriwan Radio
</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    
<nav class="navbar navbar-default">
    <div class="container">
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li><a href="/">Главная</a></li>
                <li><a href="/add_joke">Добавить шутку</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                
                <li><a href="/login">Войти</a></li>
                
            </ul>
        </div>
    </div>
</nav>

    
    




<div class="container">
    <div class="text-center">
        <h1>Podcast Main page: RSS feed</h1>
    </div>


    
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </body>
</html>

'''
