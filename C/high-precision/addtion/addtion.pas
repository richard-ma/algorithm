program addtion;
var
    str1, str2: string;
    a, b: array[1..100] of integer;
    l1, l2, i, j, k: integer;
begin
    assign(input, '');
    assign(output, '');
    reset(input);
    rewrite(output);

    readln(str1);
    readln(str2);

    l1 := length(str1);
    l2 := length(str2);

    if l1 > l2 then j:=l1 else j:=l2;

    k := 0;
    for i:=l1 downto 1 do
    begin
        inc(k);
        a[k] := ord(str1[i]) - ord('0');
    end;
    k := 0;
    for i:=l2 downto 1 do
    begin
        inc(k);
        b[k] := ord(str2[i]) - ord('0');
    end;

    for i:=1 to j do
    begin
        a[i] := a[i] + b[i];
        if (a[i] >= 10) then
        begin
            a[i] := a[i] - 10;
            a[i] := a[i+1] + 1;
        end;
    end;
    if (a[i+1] = 0) then dec(j);

    for i:=j+1 downto 1 do
        write(a[i]);

    close(input);
    close(output);
end.
