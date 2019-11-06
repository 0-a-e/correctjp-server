import re
from flask import Flask,request
from flask_cors import CORS
import click
import pyperclip
import random
import unicodedata

app = Flask(__name__)
CORS(app)
def text_len(text):
    count = 0
    for c in text:
        count += 2 if unicodedata.east_asian_width(c) in 'FWA' else 1
    return count
@app.route('/')
def trans_word2():
    inputtext = request.args.get("text")
    replacements = {
'多':'乡',
'鳥':'乌',
'雨':'丽',
'両':'两',
'並':'业',
'メルカリ':'淘宝網',
'AQUOS':'HUAWEI',
'aquos':'HUAWEI',
'Aquos':'HUAWEI',
'huaweimk':'ファーウェイウェイ',
'あなた':'貴様',
'貴':'贵',
'し':'レ',
'ぶ':'ふ',
'で':'て',
'応':'应',
'ス':'ヌ',
'雑':'杂',
'貨':'货',
'見':'见',
'潰':'溃',
'め':'ぬ',
'キ':'ギ',
'ぞ':'そ',
'舐':'舐',
'絶':'绝',
'対':'对',
'得':'慧',
'溜':'贮',
'達':'们',
'jp':'cn',
'NHK':'CCTV',
'XPERIA':'HUAWEI',
'円':'人民元',
'LINEpay':'alipay',
'PayPay':'WechatPay',
'Twitter':'weibo',
'ツイッター':'ウェイボ',
'instagram':'Tiktok',
'インスタ':'Tiktok',
'ライン':'wechat',
'LINE':'wechat',
'line':'wechat',
'風':'风',
'なさい':'(しなさい)',
'強':'强',
'東京':'北京',
'シリコンバレー':'深圳',
'google':'百度',
'グーグル':'百度',
'Google':'百度',
'スカイツリー':'上海中心',
'SKY TREE':'shanghai tower',
'TOKYO':'上海',
'ハ':'八゜',
'amazon':'亚马逊',
'アマゾン':'亚马逊',
'乘':'乘',
'黑':'黑',
'snapdragon':'Kirin',
'SD':'NM',
'PUBG':'荒野行動',
'労働':'極度勞動',
'東':'东',
'ラーメン':'うーメソ',
'🇯🇵':'🇨🇳',
'🇰🇷':'🇨🇳',
'🇺🇸':'🇨🇳',
'🇬🇧':'🇨🇳',
'🇷🇺':'🇨🇳',
'🇩🇪':'🇨🇳',
'🇮🇳':'🇨🇳',
'🇿🇦':'🇨🇳',
'🇧🇷':'🇨🇳',
'オ':'才',
'愛':'爱',
'語':'语',
'ぬ':'ゐ',
'る':'ゑ',
'iphone':'HUAWEI',
'アイフォン':'ファーウェイ',
'だ':'た',
'変':'變',
'榮':'荣',
'強':'强',
'う':'ラ',
'ハ':'八',
'応':'应',
'偉':'伟',
'義':'义',
'結':'结',
'協':'协',
'調':'调',
'剤':'剂',
'様':'樣',
'セ':'乜',
'動':'动',
'評':'评',
'ファーウェイ':'华为技术有限公司',
'HUAWEI':'华为技术有限公司'}
    if inputtext:
        print('({})'.format('|'.join(map(re.escape, replacements.keys()))))
        return re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], inputtext)
    else:
        return "servererror"
@app.route('/app')
def aprt():
    inputtext = request.args.get("text")
    apr = {
        '🇯🇵':'🇨🇳',
        'アメリカ':'美国',
        'ラーメン':'うーメソ',
        '為':'为','HUAWEI':'华为技术有限公司',
        'Huawei':'华为技术有限公司',
        'ファーウェイ':'华为技术有限公司',
        'スペック':'ﾇﾍﾟｯｹ',
        'グ':'ゲ',
        '国':'國',
        'し':'レ',
        '偽':'伪',
        '雑':'杂','貨':'货','書':'书','る':'ゑ','う':'ラ','ス':'ヌ','語':'语','く':'ㄑ',
        '貴':'贵',
        '様':'樣','応':'应','見':'见','ン':'ソ','ね':'れ','魚':'鱼','シ':'ツ゚','ル':'儿','オ':'才','勝':'胜','HONOR':'荣耀','Honor':'荣耀',
        'Google':'谷歌','綺':'绮','Balong':'巴龙','Ascend':'昇騰','Kunpeng':'鯤鵬','麗':'丽','あなた':'贵樣','贵方':'贵樣','お前':'贵樣','あんた':'贵樣','恋':'戀',
        'ヨ':'彐','ョ':'彐','浜':'滨','濱':'滨','濵':'滨','沢':'泽','澤':'泽','私':'仆','あたし':'仆','わたし':'仆','わたくし':'仆','当':'當','で':'て',
        '額':'额','す':'ず','尋':'寻','湯':'汤','00円':'00日元','の':'ゐ','リ':'刂','り':'リ','ズ':'ス','ッ':'シ','続':'续','気':'气','ボ':'㝳','購':'购',
        '買':'买','ベ':'へ','許':'许','絵':'绘','長':'长','覚':'觉','錯':'错','開':'开','評':'评','華':'华','約':'约','預':'预','乾燥':'极度干燥','間':'间',
        '飛':'飞','時':'时','伝':'传','テ':'亍','ジ':'ヅ','頼':'赖','結':'结','論':'论','悪':'恶','ゼ':'乜','セ':'乜','話':'话','電':'电','状':'狀',
        '険':'險','財':'财','声':'聲','動':'动','メ':'〆','変':'变','記':'记','号':'號','監':'监','韓':'韩','簡':'简','較':'较','顔':'颜','愛':'爱',
        '違':'违','総':'總','届':'屆','学':'學','獣':'獸','岡':'冈','輩':'辈','親':'亲','乗':'乘','ハ':'八','ミ':'シ','ク':'ケ','なさい':'(しなさい)','会':'會',
        'ア':'マ','楽':'乐','偉':'伟','パ':'八゜','際':'际','揮':'毫','来':'來','ペ':'へ','エ':'卫','ェ':'卫','労働':'極度勞動（しなさい）','風':'风','東':'东','経':'经','両':'两','拡':'扩','戦':'战','務':'务','カ':'力','か':'カ','夢':'梦','調':'调','Amazon':'亚马逊','潰':'溃','選':'选','関':'关','値':'價','義':'义','体':'體','黒':'黑','須':'须','報':'报','想像':'極度想像（しなさい）','強':'强','確':'确','税':'稅','軽':'轻','ヒ':'匕','編':'编','それ':'そね','対':'对','殺':'杀','書':'畫','進':'进','飲':'饮','議':'议','壊':'坏','Yahoo! News':'カフー二ューヌ','偵':'侦','コナソ':'ゴメソ','協':'协','温':'溫','厳':'嚴','遊':'游','黄':'黃','僕':'仆','純':'纯','習':'习','緒':'绪','潤':'润','質':'质','証':'證','内':'內','焼':'燒','軍':'军','艦':'舰','勧':'勸','売':'卖','増':'增','員':'员','🎌':'🇨🇳','🇦🇺':'🇨🇳','🇰🇷':'🇨🇳','島':'岛','熱':'热','歴':'历','満':'满','統':'统','銀':'银','綾':'绫','団':'团','過':'过','読':'读','癒':'愈','覧':'览','前代未聞':'前所未有','知恵':'智慧','Da Zhang Wei':'大张伟','Da ZhangWei':'大张伟','Da Zhangwei':'大张伟','Wowkie Zhang':'Da Zhang Wei','人间精品':'人间精品起來嗨','飯':'饭','Xperia':'Huawei','AQUOS':'HUAWEI','終':'终','TBS':'CCTV','縦':'纵','覚':'覺','大变だ':'大變た','ロゲイン':'登录','録':'录','隊':'队','トトロ':'ドドロ','ちん':'ㄘん','イ':'亻','レ(しなさい)':'(しなさい)','((':'(','))':')','（(':')',')）':'(','ツ亻シター':'ツイター','ⓃⒽⓀ':'ⓀⓈⓂ','紅':'红','済':'济',
        '決':'决','ダ亻ソー':'名創優品','NHK':'KSM','极度':'極度','静':'靜'
    }
    if inputtext:
        print('({})'.format('|'.join(map(re.escape, apr.keys()))))
        return re.sub('({})'.format('|'.join(map(re.escape, apr.keys()))), lambda m: apr[m.group()], inputtext)
    else:
        return "servererror"
@app.route('/totuzensi')
def totuzensi():
    msg = request.args.get("text")
    length = text_len(msg)
    generating = '＿人'
    for i in range(length//2):
        generating += '人'
    generating += '人＿\n＞  ' + msg + '  ＜\n￣^Y'
    for i in range(length//2):
        generating += '^Y'
    generating += '^Y￣'
    return generating
@app.route('/reverse')
def rev():
    inputtext = request.args.get("text")
    replacements = {
'乡':'多','乌':'鳥','丽':'雨','两':'両','业':'並','淘宝網':'メルカリ','HUAWEI':'AQUOS','HUAWEI':'aquos','HUAWEI':'Aquos',
'ファーウェイウェイ':'huaweimk','貴様':'あなた','贵':'貴','レ':'し','ふ':'ぶ','て':'で','应':'応','ヌ':'ス','杂':'雑','货':'貨','见':'見',
'溃':'潰','ぬ':'め','ギ':'キ','そ':'ぞ','舐':'舐','绝':'絶','对':'対','慧':'得','贮':'溜','们':'達','cn':'jp','CCTV':'NHK',
'HUAWEI':'XPERIA','人民元':'円','alipay':'LINEpay','WechatPay':'PayPay','weibo':'Twitter','ウェイボ':'ツイッター','Tiktok':'instagram',
'Tiktok':'インスタ','wechat':'ライン','wechat':'LINE','wechat':'line','风':'風','(しなさい)':'なさい','强':'強','北京':'東京',
'深圳':'シリコンバレー','百度':'google','百度':'グーグル','百度':'Google','上海中心':'スカイツリー','shanghai tower':'SKY TREE',
'上海':'TOKYO','八゜':'ハ','亚马逊':'amazon','亚马逊':'アマゾン','乘':'乘','黑':'黑','Kirin':'snapdragon',
'NM':'SD','荒野行動':'PUBG','極度勞動':'労働','东':'東','うーメソ':'ラーメン',
'🇨🇳':'🇯🇵','🇨🇳':'🇰🇷','🇨🇳':'🇺🇸','🇨🇳':'🇬🇧','🇨🇳':'🇷🇺','🇨🇳':'🇩🇪','🇨🇳':'🇮🇳','🇨🇳':'🇿🇦','🇨🇳':'🇧🇷','才':'オ',
'爱':'愛','语':'語','ゐ':'ぬ','ゑ':'る','HUAWEI':'iphone','ファーウェイ':'アイフォン','た':'だ','變':'変','荣':'榮','强':'強',
'ラ':'う','八':'ハ','应':'応','伟':'偉','义':'義','结':'結','协':'協','调':'調','剂':'剤',
'樣':'様','乜':'セ','动':'動','评':'評','华为技术有限公司':'ファーウェイ','华为技术有限公司':'HUAWEI'
}
    if inputtext:
        print('({})'.format('|'.join(map(re.escape, replacements.keys()))))
        return re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], inputtext)
    else:
        return "servererror"
@app.route('/ALIEN')
def alien():
    inputtext = request.args.get("text")
    replacements = {
        'A':'𝐀','B':'𝐁','C':'𝐂','D':'𝐃','E':'𝐄','F':'𝐅','G':'𝐆','H':'𝐇','I':'𝐈','J':'𝐉',
        'K':'𝐊','M':'𝐌','N':'𝐍','O':'𝐎','P':'𝐏','Q':'𝐐','R':'𝐑','S':'𝐒','T':'𝐓','U':'𝐔','V':'𝐕','W':'𝐖',
        'X':'𝐗','Y':'𝐘','Z':'𝐙','1':'𝟏','2':'𝟐','3':'𝟑','4':'𝟒',
        '5':'𝟓','6':'𝟔','7':'𝟕',
        '8':'𝟖','9':'𝟗','0':'𝟎'
        }
    if inputtext:
        print('({})'.format('|'.join(map(re.escape, replacements.keys()))))
        return re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], inputtext)
    else:
        return "servererror"
@app.route('/falcon')
def falcon():
    l = ['フ','ァ','ル','コ','ン','・','パ','ン','チ']
    res = random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l) + random.choice(l)
    return res
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)