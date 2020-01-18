class Evaluator:
    def zip_evaluate(coefs, words):
        if type(words) is not list or type(coefs) is not list or len(words) != len(coefs):
            return -1
        li = list(zip(coefs, words))
        lensum = 0
        for i in range(len(li)):
            lensum += li[i][0] * len(li[i][1])
        print(lensum)

    def enumerate_evaluate(coefs, words):
        if type(words) is not list or type(coefs) is not list or len(words) != len(coefs):
            return -1
        coefs_li = dict(enumerate(coefs))
        words_li = dict(enumerate(words))
        lensum = 0
        for key in coefs_li.keys():
            lensum += coefs_li[key] * len(words_li[key])
        print(lensum)


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)
