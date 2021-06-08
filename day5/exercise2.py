
def max_score(scores):
    max_score = 0
    for score in scores:
        if score > max_score: max_score = score
    
    return max_score

def run():
    studen_scores = input("Input a list of student scores ").split()
    for n in range(0, len(studen_scores)):
        studen_scores[n] = int(studen_scores[n])
    
    # Method native python
    print(max(studen_scores))
    # Method not native python
    print(max_score(studen_scores))

if __name__ == "__main__":
    run()