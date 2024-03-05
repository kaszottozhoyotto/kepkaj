{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "w1p9yJE8mlrj"
      },
      "outputs": [],
      "source": [
        "import re\n",
        "\n",
        "class StringCalculator:\n",
        "    def __init__(self, name, age):\n",
        "      self.name = name\n",
        "      self.age = age\n",
        "\n",
        "    def Calculate(string):\n",
        "      if(string == None):\n",
        "        return 0\n",
        "\n",
        "      delimiters = [',', '\\n']\n",
        "\n",
        "      #if(string.startswith('//')):\n",
        "\n",
        "\n",
        "      output = re.findall(\"//\\[(.*?)\\]\",string)\n",
        "      for o in output:\n",
        "        o.replace('/','')\n",
        "        o.replace('[','')\n",
        "        o.replace(']','')\n",
        "        delimiters.append(o)\n",
        "\n",
        "      string = string.replace('/','')\n",
        "      string =string.replace('[','')\n",
        "      string =string.replace(']','')\n",
        "\n",
        "      for delimiter in delimiters:\n",
        "        string = \" \".join(string.split(delimiter))\n",
        "\n",
        "      result = string.split()\n",
        "\n",
        "      sum = 0\n",
        "      for substring in result:\n",
        "        if(int(substring)>1000):\n",
        "          continue\n",
        "        if(int(substring)<0):\n",
        "          raise Exception(\"Sorry, no numbers below zero\")\n",
        "        sum += int(substring)\n",
        "\n",
        "      return sum\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "GKBxXRzHsX2P"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def Test():\n",
        "  calculator = StringCalculator\n",
        "\n",
        "  assert calculator.Calculate(None) == 0\n",
        "\n",
        "  assert calculator.Calculate('356') == 356\n",
        "\n",
        "  assert calculator.Calculate('20,10') == 30\n",
        "\n",
        "  assert calculator.Calculate('20\\n30') == 50\n",
        "\n",
        "  assert calculator.Calculate('30,50,10') == 90\n",
        "\n",
        "  assert calculator.Calculate('30,50,10000') == 80\n",
        "\n",
        "  assert calculator.Calculate('//[#]30,50#10XD10//[XD]') == 100\n",
        "Test()\n"
      ],
      "metadata": {
        "id": "zxnsvTdhm6Qe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import unittest\n",
        "\n",
        "class MyTestCase(unittest.TestCase):\n",
        "    def test(self):\n",
        "        with self.assertRaises(Exception) as context:\n",
        "            StringCalculator.Calculate('-10,10,10')\n",
        "\n",
        "        self.assertTrue('This is broken' in context.exception)\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    unittest.main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "id": "c4oU5bxdm6TF",
        "outputId": "8b8f4b42-ddcd-43c8-feca-7ba3f735d099"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "E\n",
            "======================================================================\n",
            "ERROR: /root/ (unittest.loader._FailedTest)\n",
            "----------------------------------------------------------------------\n",
            "AttributeError: module '__main__' has no attribute '/root/'\n",
            "\n",
            "----------------------------------------------------------------------\n",
            "Ran 1 test in 0.003s\n",
            "\n",
            "FAILED (errors=1)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "SystemExit",
          "evalue": "True",
          "traceback": [
            "An exception has occurred, use %tb to see the full traceback.\n",
            "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m True\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/IPython/core/interactiveshell.py:3561: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
            "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S5MH-yJrm6WG",
        "outputId": "f3798a49-1317-4b82-9351-9871dade4fe7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['123', '123', '123']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "AvV1JbHZm6ZV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "0nyBMObpm6b2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "    def Caluclate2delimited(string, split_character):\n",
        "      string_splited = string.split(split_character)\n",
        "      if(len(string_splited)==0):\n",
        "        return 0\n",
        "      if(len(string_splited)==1):\n",
        "        if(string.isdigit()):\n",
        "          return int(string)\n",
        "      if(len(string_splited)==2):\n",
        "        return int(string_splited[0]) + int(string_splited[1])\n"
      ],
      "metadata": {
        "id": "T3qVHAskm6eV"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}