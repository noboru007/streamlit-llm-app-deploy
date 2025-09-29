import os
# from google.colab import userdata
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

# 環境変数をロード
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLMの初期化
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


# Streamlitを使い、LLM機能を搭載したWebアプリ（LLMアプリ）を開発し、デプロイしましょう。
st.title("Streamlit + LLM アプリ")
st.write("このアプリは、OpenAIのGPT-4o-miniモデルを使用して、ユーザーの質問に答えます。")
st.divider()

# ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変えてください。
expertise_area = st.radio("専門家の種類を選択してください。", ["ファッションスタイリスト", "旅行ガイド", "料理研究家"])

if expertise_area == "ファッションスタイリスト":
    system_message_content = "あなたは優秀なファッションスタイリストです。"
elif expertise_area == "旅行ガイド":
    system_message_content = "あなたは経験豊富な旅行ガイドです。"
elif expertise_area == "料理研究家":
    system_message_content = "あなたは創造的な料理研究家です。"
else:
    system_message_content = "あなたは知識豊富なアシスタントです。" # デフォルトのメッセージ

# ユーザーの質問をテキスト入力で受け取る
user_question = st.text_input("あなたの質問を入力してください。")

messages = [
    SystemMessage(content=system_message_content),
    HumanMessage(content=user_question),
]
if st.button("質問を送信"):

    st.divider()

    if user_question.strip() == "":
        st.error("質問を入力してください。")
    else:
        try:
            # LLMに質問を送信し、回答を取得
            response = llm(messages)
            st.write("### 回答:")
            st.write(response.content)
        except Exception as e:
            st.error(f"LLMへの問い合わせ中にエラーが発生しました: {e}")
            print(f"エラーが発生しました: {e}")
            print(f"予期しないエラー: {e}")



# st.write("### デバッグ情報:")
# st.write(f"システムメッセージ: {system_message_content}")
# st.write(f"ユーザーの質問: {user_question}")  
# st.write(f"LLMの応答: {response.content if 'response' in locals() else 'まだ応答がありません。'}")
# st.write(f"OPENAI_API_KEY: {'設定されています' if OPENAI_API_KEY else '設定されていません'}")
# st.write(f"LLMオブジェクト: {llm}")
# st.write(f"LLMモデル名: {llm.model_name if llm else 'LLMが初期化されていません。'}")
# st.write(f"LLM温度: {llm.temperature if llm else 'LLMが初期化されていません。'}")
# st.write(f"LLMのAPIキー: {'設定されています' if llm and llm.api_key else '設定されていません'}")
# st.write(f"LLMのAPIベース: {llm.api_base if llm else 'LLMが初期化されていません。'}")
# st.write(f"LLMのAPIバージョン: {llm.api_version if llm else 'LLMが初期化されていません。'}")
# st.write(f"LLMのAPIタイプ: {llm.api_type if llm else 'LLMが初期化されていません。'}")
