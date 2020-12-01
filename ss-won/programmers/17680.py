def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = list(map(lambda x: x.lower(), cities))

    if cacheSize == 0:
        answer = len(cities) * 5
        return answer

    for city in cities:
        # cache hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        # cache miss
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
                cache.append(city)
            else:
                cache.append(city)
            answer += 5

    return answer
