from command.rootCommand import rootCommand

class help():
    def __init__(self):
        print("help : コマンド一覧")
        print("info [id] : 予約している人の情報表示")
        print("guests :  予約している人全員の情報を表示")
        print("change [id] [変更する行] [変更内容] : 既存のデータを変更")
        print("end : 初期画面に戻る")
        print("\n")
        rootCommand.rootCommand().root_command()