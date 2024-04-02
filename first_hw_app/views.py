import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def greet(request):
    html = """
        <div style='margin: auto; width: 50vw; text-align: center;'>
            <h1> Main page </h1>
            <div style='margin-top: 10vh'>
                <h3>
                    My first django app
                </h3>
            </div>
            <div>
                <a href='./about'>About me</a>
            </div>
        </div>
         """
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    html = """
        <div style='margin: auto; width: 50vw;'>
            <h1 style='text-align: center;'> About me </h1>
            <div style=''>
                <h3>
                   My name is Eugenia Kravets and bouldering is my passion...
                </h3>
            </div>
            <div>
                <h4>
                <p>
                А помимо скалолазания, я активно изучаю Django. (=^x^=)
                </p>
                </h4>
            </div>
        </div>
    """
    logger.info('About page accessed')
    return HttpResponse(html)
