import media
import fresh_tomatoes

# 使用类变量/常量
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)


gsd_story = media.Movie("Gongshoudao",
                        "This is a story about Tai Chi", 
                        "http://r1.ykimg.com/051600005A07EC22ADBC092D8C0A7FB4",
                        "http://v.youku.com/v_show/id_XMzE0ODM1ODg1Ng==.html")

girls_kingdom = media.Movie("The Women's Kingdom",
                        "A story of girls'kingdom", 
                        "http://r1.ykimg.com/0516000058F57159ADBAC325750F3B65",
                        "http://v.youku.com/v_show/id_XMzI2NTM2NzUwOA==.html")

Chasing_Dragon = media.Movie("Chasing the Dragon",
                        "The movie tells the story of two legend in Hong Kong's modern history", 
                        "http://r1.ykimg.com/0516000059C20B29ADBAC304A2033421",
                        "http://v.youku.com/v_show/id_XMzIzNTkyNzYyOA==.html")

Hear_Me = media.Movie("Hear Me",
                        "A touching love story", 
                        "http://r1.ykimg.com/0516000055826A2667BC3C49E7051D71",
                        "http://v.youku.com/v_show/id_XMTUxMDcxMzA2OA==.html")

KungFu_Yoga = media.Movie("Kung Fu Yoga",
                        "An adventure comedy story", 
                        "http://r1.ykimg.com/051600005824087067BC3C7C6F02B9EF",
                        "http://v.youku.com/v_show/id_XMjY1NDkzNzEzMg==.html")

Badrinath_Ki_Dulhania = media.Movie("Badrinath Ki Dulhania",
                        "A love story happened in India", 
                        "http://r1.ykimg.com/0516000059A3DA32ADBA1F9B680C4A1C",
                        "http://v.youku.com/v_show/id_XMjk5NDk1ODAxNg==.html")


# print(gsd_story.storyline)
# girls_kingdom.show_trailer()
movies = [gsd_story, girls_kingdom, Chasing_Dragon, Hear_Me, KungFu_Yoga, Badrinath_Ki_Dulhania]
fresh_tomatoes.open_movies_page(movies)