points = {
    ('A','E','I','O','U','L','N','R','S','T'):1,
    ('D','G'):2,
    ('B','C','M','P'):3,
    ('F','H','V','W','Y'):4,
    ('K'):5,
    ('J','X'):8,
    ('Q','Z'):10,
    }

def score(w):
    total = 0;
    pts = 0;
    for letter in w:
        for item in points:
            if letter in item:
                pts = points[item];
        total = total + pts;
    return total
        
print(score("HELLO"))