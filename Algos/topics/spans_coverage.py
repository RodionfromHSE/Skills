from dataclasses import dataclass, field

@dataclass(order=True)
class Span:
    l: int
    r: int






def main():
    END = int(input())
    spans = []
    while True:
        try:
            l, r = map(int, input().split())
        except (EOFError, ValueError):
            break

        l = max(l, 0)
        r = min(r, END)
        if l < r:
            spans.append(Span(l, r))
    
    if not spans or spans[0].l > 0:
        print(-1)
        return
    spans.sort()
    span_id = 0
    cur_span = spans[span_id]
    ans = [cur_span]
    n = len(spans)
    while span_id < n:
        next_span = None
        while span_id < n and spans[span_id].l <= cur_span.r:
            if spans[span_id].r > cur_span.r and (next_span is None or spans[span_id].r > next_span.r):
                next_span = spans[span_id]
            span_id += 1
        if next_span is None and (not ans or ans[-1].r < END):
            print(-1)
            return
        
        if next_span is None:
            break

        ans.append(next_span)
        cur_span = next_span
    if ans[-1].r < END:
        print(-1)
        return
    
    print(len(ans))
    print(*ans, sep='\n')
        

if __name__ == '__main__':
    main()