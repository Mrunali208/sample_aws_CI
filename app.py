from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
current_player = "X"
game_over = False
score = {"X": 0, "O": 0}

def check_winner():
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a], (a,b,c)
    if "" not in board:
        return "Draw", None
    return None, None

@app.route("/")
def index():
    return render_template("index.html", score=score)

@app.route("/move", methods=["POST"])
def move():
    global current_player, game_over, score

    if game_over:
        return jsonify({"status": "over"})

    i = int(request.form["index"])

    if board[i] == "":
        board[i] = current_player
        winner, combo = check_winner()

        if winner:
            game_over = True
            if winner != "Draw":
                score[winner] += 1

            return jsonify({
                "status": "win",
                "winner": winner,
                "combo": combo,
                "score": score
            })

        current_player = "O" if current_player == "X" else "X"

    return jsonify({
        "status": "continue",
        "player": current_player
    })

@app.route("/reset")
def reset():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True)