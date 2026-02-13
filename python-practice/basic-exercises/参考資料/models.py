from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func  # ★ADD: Postgresでも安全な日時関数

db = SQLAlchemy()


# --- Userモデル---
class User(UserMixin, db.Model):    # このUserというクラスは、DBのテーブルと対応します
    __tablename__ = "user"    # 実際のDB上のテーブル名をuserに指定

    id = db.Column(db.Integer, primary_key=True)    # 整数型で主キーのカラム
    userid = db.Column(db.String(80), unique=True, nullable=False, index=True)    # 80文字以内の短めの文字列型で、値の重複を許さない、null禁止（必須項目）、検索高速化のための目次
    # ▲ 本来はunique=Trueがあれば自動でindex作成されるけど、将来unique=Trueじゃなくしたときもindexが使えるようにしておく
    password_hash = db.Column(db.String(255), nullable=False)    # 255文字以内の短めの文字列型で、null禁止（必須項目）※平文で保存せずハッシュ化
    
    # 作成日時カラム（業務アプリではほぼ必須）
    created_at = db.Column(
        db.DateTime(timezone=True),    # 日時型（UTCを意識した日時）
        server_default=func.now(),   # レコード作成時に自動で現在時刻を入れる
        nullable=False     # 常に値のある状態にする（運用が楽）
    )

    # 更新日時カラム（業務アプリではほぼ必須）
    updated_at = db.Column(
        db.DateTime(timezone=True),    # 日時型（UTCを意識した日時）
        server_default=func.now(),    # レコード作成時に自動で現在時刻を入れる
        onupdate=func.now(),    # Updateが発生したら、自動で現在時刻に更新する
        nullable=False     # 常に値のある状態にする（運用が楽）
    )    

    # Userクラス専用の、パスワードをハッシュ化するメソッド　signup（ユーザー作成）のときに使用
    # Userクラスのメソッドset_passwordを定義。引数はUserインスタンス自身、パスワード（文字列型）。戻り値の型ヒント（アノテーション）：戻り値なし（noneを返す）
    def set_password(self, password: str) -> None:
        # ツール関数generate_password_hashに、ユーザーが入力した平文のパスワードを渡してハッシュ化した文字列をself.password_hash（DBカラム）に保存する
        self.password_hash = generate_password_hash(password)

    # パスワードを照合するメソッド　login（ログイン）のときに使用
    # Userクラスのメソッドcheck_passwordを定義。引数はUserインスタンス自身、パスワード（文字列型）。戻り値の型ヒント：bool型
    def check_password(self, password: str) -> bool:
        # ツール関数check_password_hashに、DBに保存されているハッシュ化されたパスワードと、ユーザーが入力した平文のパスワードを渡して照合した結果を返す（true/false）
        return check_password_hash(self.password_hash, password)

    # デバッグ、Flaskシェル、ログ出力した際に、オブジェクトを「User 3」のように短くわかりやすく表すための関数
    def __repr__(self) -> str:
        return f"<User {self.userid}>"
    

# --- Memoモデル ---
class Memo(db.Model):    # 「このMemoというクラスは、DBのテーブルと対応します」
    __tablename__ = "memo"    # 実際のDB上のテーブル名をmemoに指定

    id = db.Column(db.Integer, primary_key=True)    # 「memoテーブルには、整数型のid列があり、主キーです」
    title = db.Column(db.String(200), nullable=False)    # 「memoテーブルには、短めの文字列（200文字上限）でnull禁止（必須項目）のtitle列があります」
    body = db.Column(db.Text, nullable=False)    # 「memoテーブルには、長さ無制限の文字列でnull禁止（必須項目）のbody列があります」

    # 作成日時カラム（業務アプリではほぼ必須）
    created_at = db.Column(
        db.DateTime(timezone=True),    # 日時型（UTCを意識した日時）
        server_default=func.now(),   # レコード作成時に自動で現在時刻を入れる
        nullable=False     # 常に値のある状態にする（運用が楽）
    )

    # 更新日時カラム（業務アプリではほぼ必須）
    updated_at = db.Column(
        db.DateTime(timezone=True),    # 日時型（UTCを意識した日時）
        server_default=func.now(),    # レコード作成時に自動で現在時刻を入れる
        onupdate=func.now(),    # Updateが発生したら、自動で現在時刻に更新する
        nullable=False     # 常に値のある状態にする（運用が楽）
    )    

    # デバッグ、Flaskシェル、ログ出力した際に、オブジェクトを「Memo 3」のように短くわかりやすく表すための関数
    def __repr__(self) -> str:
        return f"<Memo {self.id}>"