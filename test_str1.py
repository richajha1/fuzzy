import sys
import psycopg2
def get_bigrams(string):
    '''
    Takes a string and returns a list of bigrams
    '''
    s = string.lower()
    return [s[i:i+2] for i in xrange(len(s) - 1)]

def user_input():
    """
    The method takes two strings from the user.
    Supports Python version <= 2.7 and >= 3.3.

    :return: It returns two input strings from the user.
    """
    """conn = psycopg2.connect(database="postgres", user="richa", password="richa")
    cursor1 = conn.cursor()
    cursor1.execute("SELECT add1||add2 FROM test1;")
    t = cursor1.fetchall()
    for i in t:
        for j in t:
             print i,j"""
    if sys.hexversion > 0x03000000:
        return input(), input()
    else:
        return raw_input(), raw_input()

def string_similarity(str1, str2):
    '''
    Perform bigram comparison between two strings
    and return a percentage match in decimal form
    '''
    pairs1 = get_bigrams(str1)
    pairs2 = get_bigrams(str2)
    union  = len(pairs1) + len(pairs2)
    hit_count = 0
    for x in pairs1:
        for y in pairs2:
            if x == y:
                hit_count += 1
                break
    return (2.0 * hit_count) / union

if __name__ == "__main__":
    conn = psycopg2.connect(database="postgres", user="richa", password="richa")
    cursor1 = conn.cursor()
    cursor1.execute("SELECT add1||add2 FROM test1;")
    t = cursor1.fetchall()
    for s1 in t:
        for s2 in t:
             sim = string_similarity(str(s1), str(s2))
	     if sim>=0.7 :
                 print s1,s2,sim
		 print
