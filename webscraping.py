{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "webscraping.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNctC3lUvv29xV3zCII5TZf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/leonardodrigo/datasets/blob/master/webscraping.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yI90Mm_I1vIA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "!pip install requests\n",
        "!pip install beautifulsoup4"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "udU4eih8RYMP",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-sp7Vv2YQ6Qc",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "url = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5vYTRG8-Rd44",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 88
        },
        "outputId": "212140a4-c789-4950-c57f-38e756f23d73"
      },
      "source": [
        "#imprimindo os primeiros 500 caracteres\n",
        "print(url.text[0:500])"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<!DOCTYPE html>\n",
            "<!--[if (gt IE 9)|!(IE)]> <!--><html lang=\"en\" class=\"no-js page-interactive section-opinion page-theme-standard tone-opinion page-interactive-default limit-small layout-xlarge app-interactive\" itemid=\"https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html\" itemtype=\"http://schema.org/NewsArticle\" itemscope xmlns:og=\"http://opengraphprotocol.org/schema/\"><!--<![endif]-->\n",
            "<!--[if IE 9]> <html lang=\"en\" class=\"no-js ie9 lt-ie10 page-interactive section-opinion page\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nYSzNku6R_Up",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "soup = BeautifulSoup(url.text, 'html.parser')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JOt2bArmWjc3",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "07a00cb7-a92b-4e1c-fac9-76d0596ae349"
      },
      "source": [
        "#Estamos verificando quantos registros temos no código conforme a estrutura do código da página em HTML\n",
        "results = soup.find_all('span', attrs={'class':'short-desc'})\n",
        "len(results)"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "180"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mGcLcu2cX9-s",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        },
        "outputId": "508ee724-f729-420d-e4e6-bdc7954ae20a"
      },
      "source": [
        "#Checando os registros\n",
        "results[-1]"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<span class=\"short-desc\"><strong>Nov. 11 </strong>“I'd rather have him  – you know, work with him on the Ukraine than standing and arguing about whether or not  – because that whole thing was set up by the Democrats.” <span class=\"short-truth\"><a href=\"https://www.nytimes.com/interactive/2017/12/10/us/politics/trump-and-russia.html\" target=\"_blank\">(There is no evidence that Democrats \"set up\" Russian interference in the election.)</a></span></span>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i9TWA_3Taieo",
        "colab_type": "text"
      },
      "source": [
        "**Extraindo a data do código**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "viXQNLMMZbX9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "33d14067-ad7d-4dcc-d719-3099fb18c0aa"
      },
      "source": [
        "#Queremos pegar a data entre as tags 'strong'\n",
        "results[0].find('strong')"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<strong>Jan. 21 </strong>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_cXZFnG0ZsHY",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "3f378714-32b1-4df0-8ca7-4864e56944e9"
      },
      "source": [
        "results[0].find('strong').text"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Jan. 21\\xa0'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SNyqs5pMZ6_6",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "6e8eed69-cf80-404e-9961-2d09f130eab2"
      },
      "source": [
        "results[0].find('strong').text[0:7] + ', 2017'"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Jan. 21, 2017'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vDLWxKw0a9Aj",
        "colab_type": "text"
      },
      "source": [
        "**Extraindo a frase do Trump**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bkf_anNdbGDl",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 88
        },
        "outputId": "bd045e74-1115-4bda-a2e2-a3319129462d"
      },
      "source": [
        "results[0].contents"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<strong>Jan. 21 </strong>,\n",
              " \"“I wasn't a fan of Iraq. I didn't want to go into Iraq.” \",\n",
              " <span class=\"short-truth\"><a href=\"https://www.buzzfeed.com/andrewkaczynski/in-2002-donald-trump-said-he-supported-invading-iraq-on-the\" target=\"_blank\">(He was for an invasion before he was against it.)</a></span>]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HM-DcfYMbgZu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "b93c4398-4f15-456b-dc3e-efbb9d6842b6"
      },
      "source": [
        "#Pegando o segundo elemento da lista (Child)\n",
        "results[0].contents[1]"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"“I wasn't a fan of Iraq. I didn't want to go into Iraq.” \""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rRScxj8dbw6A",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "061968ed-efff-4773-c404-ba8105627f40"
      },
      "source": [
        "results[0].contents[1][1:-2]"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"I wasn't a fan of Iraq. I didn't want to go into Iraq.\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oYsL9aIhgTUa",
        "colab_type": "text"
      },
      "source": [
        "**Extraindo a explicação**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zPVeqoC9hFLw",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        },
        "outputId": "eebdadb7-6b29-4263-a5c4-25766ac1eed9"
      },
      "source": [
        "results[0].find('a')"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<a href=\"https://www.buzzfeed.com/andrewkaczynski/in-2002-donald-trump-said-he-supported-invading-iraq-on-the\" target=\"_blank\">(He was for an invasion before he was against it.)</a>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yd9xF5RYiFDc",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "660804a7-0133-4960-dcca-0291ce542b89"
      },
      "source": [
        "results[0].find('a').text[1:-1]"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'He was for an invasion before he was against it.'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GRpdqpNTiVLr",
        "colab_type": "text"
      },
      "source": [
        "**Extraindo a URL**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3rvZxbmhiYC1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "dc10f22c-34fd-4fd5-e4f4-5aa77fbf710a"
      },
      "source": [
        "results[0].find('a')['href']"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'https://www.buzzfeed.com/andrewkaczynski/in-2002-donald-trump-said-he-supported-invading-iraq-on-the'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZVBsThBojN_b",
        "colab_type": "text"
      },
      "source": [
        "**Construindo o Dataset**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tJ3NcBuGjR_W",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "records = []\n",
        "for result in results:\n",
        "  date = result.find('strong').text[0:-1] + ', 2017'\n",
        "  lie = result.contents[1][1:-2]\n",
        "  explanation = result.find('a').text[1:-1]\n",
        "  url = result.find('a')['href']\n",
        "\n",
        "  records.append((date, lie, explanation, url))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ij4zgSmJkSsd",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "06b8a799-11fd-46c7-ce0f-e7eb58676d1c"
      },
      "source": [
        "len(records)"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "180"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "avEiPQullqN3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "34UkIz73mLXU",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "df['date'] = pd.to_datetime(df['date'])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-4CLuqk5mfPR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "outputId": "b4d4e03a-44c3-4816-9879-42b26e3c205f"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>date</th>\n",
              "      <th>lie</th>\n",
              "      <th>explanation</th>\n",
              "      <th>url</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2017-01-21</td>\n",
              "      <td>I wasn't a fan of Iraq. I didn't want to go in...</td>\n",
              "      <td>He was for an invasion before he was against it.</td>\n",
              "      <td>https://www.buzzfeed.com/andrewkaczynski/in-20...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2017-01-21</td>\n",
              "      <td>A reporter for Time magazine — and I have been...</td>\n",
              "      <td>Trump was on the cover 11 times and Nixon appe...</td>\n",
              "      <td>http://nation.time.com/2013/11/06/10-things-yo...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2017-01-23</td>\n",
              "      <td>Between 3 million and 5 million illegal votes ...</td>\n",
              "      <td>There's no evidence of illegal voting.</td>\n",
              "      <td>https://www.nytimes.com/2017/01/23/us/politics...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2017-01-25</td>\n",
              "      <td>Now, the audience was the biggest ever. But th...</td>\n",
              "      <td>Official aerial photos show Obama's 2009 inaug...</td>\n",
              "      <td>https://www.nytimes.com/2017/01/21/us/politics...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2017-01-25</td>\n",
              "      <td>Take a look at the Pew reports (which show vot...</td>\n",
              "      <td>The report never mentioned voter fraud.</td>\n",
              "      <td>https://www.nytimes.com/2017/01/24/us/politics...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "        date  ...                                                url\n",
              "0 2017-01-21  ...  https://www.buzzfeed.com/andrewkaczynski/in-20...\n",
              "1 2017-01-21  ...  http://nation.time.com/2013/11/06/10-things-yo...\n",
              "2 2017-01-23  ...  https://www.nytimes.com/2017/01/23/us/politics...\n",
              "3 2017-01-25  ...  https://www.nytimes.com/2017/01/21/us/politics...\n",
              "4 2017-01-25  ...  https://www.nytimes.com/2017/01/24/us/politics...\n",
              "\n",
              "[5 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MWSVLl4Um57U",
        "colab_type": "text"
      },
      "source": [
        "**Exportando o dataset para CSV**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Q-n5Me7Hm_JD",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "df.to_csv('trump_lies.csv', index=False, encoding='utf-8')"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}