# langsa-system：浪飒（langsa）进制
## 安装
```sh
pip install langsa-system
```

## demo

```python
from langsa_system.langsa import encode_langsa,decode_langsa
from langsa_system.浪飒 import encode_Langsa,decode_Langsa

print(encode_langsa("langsasec"))
print(decode_langsa(encode_langsa("langsasec")))
print(encode_Langsa("langsasec"))
print(decode_Langsa(encode_Langsa("langsasec")))
```

## 输出示例

```
annaanlaangaanagaglganlaaglganl2anlg
langsasec
浪飒飒浪飒飒浪浪浪飒飒浪浪浪浪飒浪飒飒浪飒飒飒浪浪飒飒浪浪飒飒飒浪飒飒飒浪浪飒飒浪飒飒浪浪浪浪飒浪飒飒飒浪浪飒飒浪飒飒浪浪飒浪飒浪飒飒浪浪浪飒飒
langsasec
```

## 浪飒(langsa)进制对照表

> https://langsa.langsasec.cn/langsa-system.html

| 十进制 |  二进制  |     浪飒进制     | 十六进制 | langsa进制 | 字符 |
| :----: | :------: | :--------------: | :------: | :--------: | :--: |
|   0    | 00000000 | 浪浪浪浪浪浪浪浪 |    00    |    0000    | NUL  |
|   1    | 00000001 | 浪浪浪浪浪浪浪飒 |    01    |    00la    | SOH  |
|   2    | 00000010 | 浪浪浪浪浪浪飒浪 |    02    |    00ln    | STX  |
|   3    | 00000011 | 浪浪浪浪浪浪飒飒 |    03    |    00lg    | ETX  |
|   4    | 00000100 | 浪浪浪浪浪飒浪浪 |    04    |    00ls    | EOT  |
|   5    | 00000101 | 浪浪浪浪浪飒浪飒 |    05    |    00l2    | ENQ  |
|   6    | 00000110 | 浪浪浪浪浪飒飒浪 |    06    |    00an    | ACK  |
|   7    | 00000111 | 浪浪浪浪浪飒飒飒 |    07    |    00ag    | BEL  |
|   8    | 00001000 | 浪浪浪浪飒浪浪浪 |    08    |    00as    |  BS  |
|   9    | 00001001 | 浪浪浪浪飒浪浪飒 |    09    |    00aa    |  HT  |
|   10   | 00001010 | 浪浪浪浪飒浪飒浪 |    0A    |    00ng    |  LF  |
|   11   | 00001011 | 浪浪浪浪飒浪飒飒 |    0B    |    00ns    |  VT  |
|   12   | 00001100 | 浪浪浪浪飒飒浪浪 |    0C    |    00na    |  FF  |
|   13   | 00001101 | 浪浪浪浪飒飒浪飒 |    0D    |    00gs    |  CR  |
|   14   | 00001110 | 浪浪浪浪飒飒飒浪 |    0E    |    00ga    |  SO  |
|   15   | 00001111 | 浪浪浪浪飒飒飒飒 |    0F    |    00sa    |  SI  |
|   16   | 00010000 | 浪浪浪飒浪浪浪浪 |    10    |    la00    | DLE  |
|   17   | 00010001 | 浪浪浪飒浪浪浪飒 |    11    |    lala    | DC1  |
|   18   | 00010010 | 浪浪浪飒浪浪飒浪 |    12    |    laln    | DC2  |
|   19   | 00010011 | 浪浪浪飒浪浪飒飒 |    13    |    lalg    | DC3  |
|   20   | 00010100 | 浪浪浪飒浪飒浪浪 |    14    |    lals    | DC4  |
|   21   | 00010101 | 浪浪浪飒浪飒浪飒 |    15    |    lal2    | NAK  |
|   22   | 00010110 | 浪浪浪飒浪飒飒浪 |    16    |    laan    | SYN  |
|   23   | 00010111 | 浪浪浪飒浪飒飒飒 |    17    |    laag    | ETB  |
|   24   | 00011000 | 浪浪浪飒飒浪浪浪 |    18    |    laas    | CAN  |
|   25   | 00011001 | 浪浪浪飒飒浪浪飒 |    19    |    laaa    |  EM  |
|   26   | 00011010 | 浪浪浪飒飒浪飒浪 |    1A    |    lang    | SUB  |
|   27   | 00011011 | 浪浪浪飒飒浪飒飒 |    1B    |    lans    | ESC  |
|   28   | 00011100 | 浪浪浪飒飒飒浪浪 |    1C    |    lana    |  FS  |
|   29   | 00011101 | 浪浪浪飒飒飒浪飒 |    1D    |    lags    |  GS  |
|   30   | 00011110 | 浪浪浪飒飒飒飒浪 |    1E    |    laga    |  RS  |
|   31   | 00011111 | 浪浪浪飒飒飒飒飒 |    1F    |    lasa    |  US  |
|   32   | 00100000 | 浪浪飒浪浪浪浪浪 |    20    |    ln00    | ' '  |
|   33   | 00100001 | 浪浪飒浪浪浪浪飒 |    21    |    lnla    |  !   |
|   34   | 00100010 | 浪浪飒浪浪浪飒浪 |    22    |    lnln    |  "   |
|   35   | 00100011 | 浪浪飒浪浪浪飒飒 |    23    |    lnlg    |  #   |
|   36   | 00100100 | 浪浪飒浪浪飒浪浪 |    24    |    lnls    |  $   |
|   37   | 00100101 | 浪浪飒浪浪飒浪飒 |    25    |    lnl2    |  %   |
|   38   | 00100110 | 浪浪飒浪浪飒飒浪 |    26    |    lnan    |  &   |
|   39   | 00100111 | 浪浪飒浪浪飒飒飒 |    27    |    lnag    |  '   |
|   40   | 00101000 | 浪浪飒浪飒浪浪浪 |    28    |    lnas    |  (   |
|   41   | 00101001 | 浪浪飒浪飒浪浪飒 |    29    |    lnaa    |  )   |
|   42   | 00101010 | 浪浪飒浪飒浪飒浪 |    2A    |    lnng    |  *   |
|   43   | 00101011 | 浪浪飒浪飒浪飒飒 |    2B    |    lnns    |  +   |
|   44   | 00101100 | 浪浪飒浪飒飒浪浪 |    2C    |    lnna    |  ,   |
|   45   | 00101101 | 浪浪飒浪飒飒浪飒 |    2D    |    lngs    |  -   |
|   46   | 00101110 | 浪浪飒浪飒飒飒浪 |    2E    |    lnga    |  .   |
|   47   | 00101111 | 浪浪飒浪飒飒飒飒 |    2F    |    lnsa    |  /   |
|   48   | 00110000 | 浪浪飒飒浪浪浪浪 |    30    |    lg00    |  0   |
|   49   | 00110001 | 浪浪飒飒浪浪浪飒 |    31    |    lgla    |  1   |
|   50   | 00110010 | 浪浪飒飒浪浪飒浪 |    32    |    lgln    |  2   |
|   51   | 00110011 | 浪浪飒飒浪浪飒飒 |    33    |    lglg    |  3   |
|   52   | 00110100 | 浪浪飒飒浪飒浪浪 |    34    |    lgls    |  4   |
|   53   | 00110101 | 浪浪飒飒浪飒浪飒 |    35    |    lgl2    |  5   |
|   54   | 00110110 | 浪浪飒飒浪飒飒浪 |    36    |    lgan    |  6   |
|   55   | 00110111 | 浪浪飒飒浪飒飒飒 |    37    |    lgag    |  7   |
|   56   | 00111000 | 浪浪飒飒飒浪浪浪 |    38    |    lgas    |  8   |
|   57   | 00111001 | 浪浪飒飒飒浪浪飒 |    39    |    lgaa    |  9   |
|   58   | 00111010 | 浪浪飒飒飒浪飒浪 |    3A    |    lgng    |  :   |
|   59   | 00111011 | 浪浪飒飒飒浪飒飒 |    3B    |    lgns    |  ;   |
|   60   | 00111100 | 浪浪飒飒飒飒浪浪 |    3C    |    lgna    |  <   |
|   61   | 00111101 | 浪浪飒飒飒飒浪飒 |    3D    |    lggs    |  =   |
|   62   | 00111110 | 浪浪飒飒飒飒飒浪 |    3E    |    lgga    |  >   |
|   63   | 00111111 | 浪浪飒飒飒飒飒飒 |    3F    |    lgsa    |  ?   |
|   64   | 01000000 | 浪飒浪浪浪浪浪浪 |    40    |    ls00    |  @   |
|   65   | 01000001 | 浪飒浪浪浪浪浪飒 |    41    |    lsla    |  A   |
|   66   | 01000010 | 浪飒浪浪浪浪飒浪 |    42    |    lsln    |  B   |
|   67   | 01000011 | 浪飒浪浪浪浪飒飒 |    43    |    lslg    |  C   |
|   68   | 01000100 | 浪飒浪浪浪飒浪浪 |    44    |    lsls    |  D   |
|   69   | 01000101 | 浪飒浪浪浪飒浪飒 |    45    |    lsl2    |  E   |
|   70   | 01000110 | 浪飒浪浪浪飒飒浪 |    46    |    lsan    |  F   |
|   71   | 01000111 | 浪飒浪浪浪飒飒飒 |    47    |    lsag    |  G   |
|   72   | 01001000 | 浪飒浪浪飒浪浪浪 |    48    |    lsas    |  H   |
|   73   | 01001001 | 浪飒浪浪飒浪浪飒 |    49    |    lsaa    |  I   |
|   74   | 01001010 | 浪飒浪浪飒浪飒浪 |    4A    |    lsng    |  J   |
|   75   | 01001011 | 浪飒浪浪飒浪飒飒 |    4B    |    lsns    |  K   |
|   76   | 01001100 | 浪飒浪浪飒飒浪浪 |    4C    |    lsna    |  L   |
|   77   | 01001101 | 浪飒浪浪飒飒浪飒 |    4D    |    lsgs    |  M   |
|   78   | 01001110 | 浪飒浪浪飒飒飒浪 |    4E    |    lsga    |  N   |
|   79   | 01001111 | 浪飒浪浪飒飒飒飒 |    4F    |    lssa    |  O   |
|   80   | 01010000 | 浪飒浪飒浪浪浪浪 |    50    |    l200    |  P   |
|   81   | 01010001 | 浪飒浪飒浪浪浪飒 |    51    |    l2la    |  Q   |
|   82   | 01010010 | 浪飒浪飒浪浪飒浪 |    52    |    l2ln    |  R   |
|   83   | 01010011 | 浪飒浪飒浪浪飒飒 |    53    |    l2lg    |  S   |
|   84   | 01010100 | 浪飒浪飒浪飒浪浪 |    54    |    l2ls    |  T   |
|   85   | 01010101 | 浪飒浪飒浪飒浪飒 |    55    |    l2l2    |  U   |
|   86   | 01010110 | 浪飒浪飒浪飒飒浪 |    56    |    l2an    |  V   |
|   87   | 01010111 | 浪飒浪飒浪飒飒飒 |    57    |    l2ag    |  W   |
|   88   | 01011000 | 浪飒浪飒飒浪浪浪 |    58    |    l2as    |  X   |
|   89   | 01011001 | 浪飒浪飒飒浪浪飒 |    59    |    l2aa    |  Y   |
|   90   | 01011010 | 浪飒浪飒飒浪飒浪 |    5A    |    l2ng    |  Z   |
|   91   | 01011011 | 浪飒浪飒飒浪飒飒 |    5B    |    l2ns    |  [   |
|   92   | 01011100 | 浪飒浪飒飒飒浪浪 |    5C    |    l2na    |  \   |
|   93   | 01011101 | 浪飒浪飒飒飒浪飒 |    5D    |    l2gs    |  ]   |
|   94   | 01011110 | 浪飒浪飒飒飒飒浪 |    5E    |    l2ga    |  ^   |
|   95   | 01011111 | 浪飒浪飒飒飒飒飒 |    5F    |    l2sa    |  _   |
|   96   | 01100000 | 浪飒飒浪浪浪浪浪 |    60    |    an00    |  `   |
|   97   | 01100001 | 浪飒飒浪浪浪浪飒 |    61    |    anla    |  a   |
|   98   | 01100010 | 浪飒飒浪浪浪飒浪 |    62    |    anln    |  b   |
|   99   | 01100011 | 浪飒飒浪浪浪飒飒 |    63    |    anlg    |  c   |
|  100   | 01100100 | 浪飒飒浪浪飒浪浪 |    64    |    anls    |  d   |
|  101   | 01100101 | 浪飒飒浪浪飒浪飒 |    65    |    anl2    |  e   |
|  102   | 01100110 | 浪飒飒浪浪飒飒浪 |    66    |    anan    |  f   |
|  103   | 01100111 | 浪飒飒浪浪飒飒飒 |    67    |    anag    |  g   |
|  104   | 01101000 | 浪飒飒浪飒浪浪浪 |    68    |    anas    |  h   |
|  105   | 01101001 | 浪飒飒浪飒浪浪飒 |    69    |    anaa    |  i   |
|  106   | 01101010 | 浪飒飒浪飒浪飒浪 |    6A    |    anng    |  j   |
|  107   | 01101011 | 浪飒飒浪飒浪飒飒 |    6B    |    anns    |  k   |
|  108   | 01101100 | 浪飒飒浪飒飒浪浪 |    6C    |    anna    |  l   |
|  109   | 01101101 | 浪飒飒浪飒飒浪飒 |    6D    |    angs    |  m   |
|  110   | 01101110 | 浪飒飒浪飒飒飒浪 |    6E    |    anga    |  n   |
|  111   | 01101111 | 浪飒飒浪飒飒飒飒 |    6F    |    ansa    |  o   |
|  112   | 01110000 | 浪飒飒飒浪浪浪浪 |    70    |    ag00    |  p   |
|  113   | 01110001 | 浪飒飒飒浪浪浪飒 |    71    |    agla    |  q   |
|  114   | 01110010 | 浪飒飒飒浪浪飒浪 |    72    |    agln    |  r   |
|  115   | 01110011 | 浪飒飒飒浪浪飒飒 |    73    |    aglg    |  s   |
|  116   | 01110100 | 浪飒飒飒浪飒浪浪 |    74    |    agls    |  t   |
|  117   | 01110101 | 浪飒飒飒浪飒浪飒 |    75    |    agl2    |  u   |
|  118   | 01110110 | 浪飒飒飒浪飒飒浪 |    76    |    agan    |  v   |
|  119   | 01110111 | 浪飒飒飒浪飒飒飒 |    77    |    agag    |  w   |
|  120   | 01111000 | 浪飒飒飒飒浪浪浪 |    78    |    agas    |  x   |
|  121   | 01111001 | 浪飒飒飒飒浪浪飒 |    79    |    agaa    |  y   |
|  122   | 01111010 | 浪飒飒飒飒浪飒浪 |    7A    |    agng    |  z   |
|  123   | 01111011 | 浪飒飒飒飒浪飒飒 |    7B    |    agns    |  {   |
|  124   | 01111100 | 浪飒飒飒飒飒浪浪 |    7C    |    agna    |  \|  |
|  125   | 01111101 | 浪飒飒飒飒飒浪飒 |    7D    |    aggs    |  }   |
|  126   | 01111110 | 浪飒飒飒飒飒飒浪 |    7E    |    agga    |  ~   |
|  127   | 01111111 | 浪飒飒飒飒飒飒飒 |    7F    |    agsa    | DEL  |

## 原理（具体参照对照表）

### 浪飒进制

浪——>0，飒——>1，类似二进制替换

### langsa进制

langsa六个字母两两组合加上00一共16种组合对应16进制的0-f，由于有两个la，所以将第二个替换为l2
