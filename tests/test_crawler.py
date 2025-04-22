import unittest
from core.crawler import parser_latest_news


class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.test_html = '''
            <div class="left_cont">
                <h2>
                    <span>
                        <font>지디넷코리아</font>에서 제공하는 최신 뉴스
                    </span>
                </h2>
                <div class="news_box">    
                    <div class="newsPost">
                        <div class="assetThumb">
                            <a href="/view/?no=20250422144400" title="">
                                <figure class="img">
                                    <img 
                                        src="https://image.zdnet.co.kr/2025/03/26/1287794536835f01d1a6e9819ab66cc3-290x182.jpg" 
                                        data-src="https://image.zdnet.co.kr/2025/03/26/1287794536835f01d1a6e9819ab66cc3-290x182.jpg" 
                                        class="lazyload" 
                                        alt="" 
                                        width="170" 
                                        height="122">
                                </figure>
                            </a>
                        </div>
                        <div class="assetText">
                            <a href="/view/?no=20250422144400">
                                <h3>테스트 뉴스 제목</h3>
                                <p>테스트 뉴스 내용 입니다</p>
                            </a>
                            <p class="byline"><span>2025.04.22 PM 03:58</span><a href="/reporter/?lstcode=jh7253">링크</a></p>
                        </div>
                    </div>
                </div>
            </div>  
        '''

    def test_parser_latest_news(self):
        result = parser_latest_news(self.test_html)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], '테스트 뉴스 제목')
        self.assertEqual(result[0]['content'], '테스트 뉴스 내용 입니다')
        self.assertEqual(result[0]['thumbnail'], 'https://image.zdnet.co.kr/2025/03/26/1287794536835f01d1a6e9819ab66cc3-290x182.jpg')


if __name__ == '__main__':
    unittest.main()
