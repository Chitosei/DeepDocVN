#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import re

TBL = {
    "2": {"name": "北京", "parent": "1"},
    "3": {"name": "天津", "parent": "1"},
    "4": {"name": "河北", "parent": "1"},
    "5": {"name": "山西", "parent": "1"},
    "6": {"name": "内蒙古", "parent": "1"},
    "7": {"name": "辽宁", "parent": "1"},
    "8": {"name": "吉林", "parent": "1"},
    "9": {"name": "黑龙江", "parent": "1"},
    "10": {"name": "上海", "parent": "1"},
    "11": {"name": "江苏", "parent": "1"},
    "12": {"name": "浙江", "parent": "1"},
    "13": {"name": "安徽", "parent": "1"},
    "14": {"name": "福建", "parent": "1"},
    "15": {"name": "江西", "parent": "1"},
    "16": {"name": "山东", "parent": "1"},
    "17": {"name": "河南", "parent": "1"},
    "18": {"name": "湖北", "parent": "1"},
    "19": {"name": "湖南", "parent": "1"},
    "20": {"name": "广东", "parent": "1"},
    "21": {"name": "广西", "parent": "1"},
    "22": {"name": "海南", "parent": "1"},
    "23": {"name": "重庆", "parent": "1"},
    "24": {"name": "四川", "parent": "1"},
    "25": {"name": "贵州", "parent": "1"},
    "26": {"name": "云南", "parent": "1"},
    "27": {"name": "西藏", "parent": "1"},
    "28": {"name": "陕西", "parent": "1"},
    "29": {"name": "甘肃", "parent": "1"},
    "30": {"name": "青海", "parent": "1"},
    "31": {"name": "宁夏", "parent": "1"},
    "32": {"name": "新疆", "parent": "1"},
    "33": {"name": "北京市", "parent": "2"},
    "34": {"name": "天津市", "parent": "3"},
    "35": {"name": "石家庄市", "parent": "4"},
    "36": {"name": "唐山市", "parent": "4"},
    "37": {"name": "秦皇岛市", "parent": "4"},
    "38": {"name": "邯郸市", "parent": "4"},
    "39": {"name": "邢台市", "parent": "4"},
    "40": {"name": "保定市", "parent": "4"},
    "41": {"name": "张家口市", "parent": "4"},
    "42": {"name": "承德市", "parent": "4"},
    "43": {"name": "沧州市", "parent": "4"},
    "44": {"name": "廊坊市", "parent": "4"},
    "45": {"name": "衡水市", "parent": "4"},
    "46": {"name": "太原市", "parent": "5"},
    "47": {"name": "大同市", "parent": "5"},
    "48": {"name": "阳泉市", "parent": "5"},
    "49": {"name": "长治市", "parent": "5"},
    "50": {"name": "晋城市", "parent": "5"},
    "51": {"name": "朔州市", "parent": "5"},
    "52": {"name": "晋中市", "parent": "5"},
    "53": {"name": "运城市", "parent": "5"},
    "54": {"name": "忻州市", "parent": "5"},
    "55": {"name": "临汾市", "parent": "5"},
    "56": {"name": "吕梁市", "parent": "5"},
    "57": {"name": "呼和浩特市", "parent": "6"},
    "58": {"name": "包头市", "parent": "6"},
    "59": {"name": "乌海市", "parent": "6"},
    "60": {"name": "赤峰市", "parent": "6"},
    "61": {"name": "通辽市", "parent": "6"},
    "62": {"name": "鄂尔多斯市", "parent": "6"},
    "63": {"name": "呼伦贝尔市", "parent": "6"},
    "64": {"name": "巴彦淖尔市", "parent": "6"},
    "65": {"name": "乌兰察布市", "parent": "6"},
    "66": {"name": "兴安盟", "parent": "6"},
    "67": {"name": "锡林郭勒盟", "parent": "6"},
    "68": {"name": "阿拉善盟", "parent": "6"},
    "69": {"name": "沈阳市", "parent": "7"},
    "70": {"name": "大连市", "parent": "7"},
    "71": {"name": "鞍山市", "parent": "7"},
    "72": {"name": "抚顺市", "parent": "7"},
    "73": {"name": "本溪市", "parent": "7"},
    "74": {"name": "丹东市", "parent": "7"},
    "75": {"name": "锦州市", "parent": "7"},
    "76": {"name": "营口市", "parent": "7"},
    "77": {"name": "阜新市", "parent": "7"},
    "78": {"name": "辽阳市", "parent": "7"},
    "79": {"name": "盘锦市", "parent": "7"},
    "80": {"name": "铁岭市", "parent": "7"},
    "81": {"name": "朝阳市", "parent": "7"},
    "82": {"name": "葫芦岛市", "parent": "7"},
    "83": {"name": "长春市", "parent": "8"},
    "84": {"name": "吉林市", "parent": "8"},
    "85": {"name": "四平市", "parent": "8"},
    "86": {"name": "辽源市", "parent": "8"},
    "87": {"name": "通化市", "parent": "8"},
    "88": {"name": "白山市", "parent": "8"},
    "89": {"name": "松原市", "parent": "8"},
    "90": {"name": "白城市", "parent": "8"},
    "91": {"name": "延边朝鲜族自治州", "parent": "8"},
    "92": {"name": "哈尔滨市", "parent": "9"},
    "93": {"name": "齐齐哈尔市", "parent": "9"},
    "94": {"name": "鸡西市", "parent": "9"},
    "95": {"name": "鹤岗市", "parent": "9"},
    "96": {"name": "双鸭山市", "parent": "9"},
    "97": {"name": "大庆市", "parent": "9"},
    "98": {"name": "伊春市", "parent": "9"},
    "99": {"name": "佳木斯市", "parent": "9"},
    "100": {"name": "七台河市", "parent": "9"},
    "101": {"name": "牡丹江市", "parent": "9"},
    "102": {"name": "黑河市", "parent": "9"},
    "103": {"name": "绥化市", "parent": "9"},
    "104": {"name": "大兴安岭地区", "parent": "9"},
    "105": {"name": "上海市", "parent": "10"},
    "106": {"name": "南京市", "parent": "11"},
    "107": {"name": "无锡市", "parent": "11"},
    "108": {"name": "徐州市", "parent": "11"},
    "109": {"name": "常州市", "parent": "11"},
    "110": {"name": "苏州市", "parent": "11"},
    "111": {"name": "南通市", "parent": "11"},
    "112": {"name": "连云港市", "parent": "11"},
    "113": {"name": "淮安市", "parent": "11"},
    "114": {"name": "盐城市", "parent": "11"},
    "115": {"name": "扬州市", "parent": "11"},
    "116": {"name": "镇江市", "parent": "11"},
    "117": {"name": "泰州市", "parent": "11"},
    "118": {"name": "宿迁市", "parent": "11"},
    "119": {"name": "杭州市", "parent": "12"},
    "120": {"name": "宁波市", "parent": "12"},
    "121": {"name": "温州市", "parent": "12"},
    "122": {"name": "嘉兴市", "parent": "12"},
    "123": {"name": "湖州市", "parent": "12"},
    "124": {"name": "绍兴市", "parent": "12"},
    "125": {"name": "金华市", "parent": "12"},
    "126": {"name": "衢州市", "parent": "12"},
    "127": {"name": "舟山市", "parent": "12"},
    "128": {"name": "台州市", "parent": "12"},
    "129": {"name": "丽水市", "parent": "12"},
    "130": {"name": "合肥市", "parent": "13"},
    "131": {"name": "芜湖市", "parent": "13"},
    "132": {"name": "蚌埠市", "parent": "13"},
    "133": {"name": "淮南市", "parent": "13"},
    "134": {"name": "马鞍山市", "parent": "13"},
    "135": {"name": "淮北市", "parent": "13"},
    "136": {"name": "铜陵市", "parent": "13"},
    "137": {"name": "安庆市", "parent": "13"},
    "138": {"name": "黄山市", "parent": "13"},
    "139": {"name": "滁州市", "parent": "13"},
    "140": {"name": "阜阳市", "parent": "13"},
    "141": {"name": "宿州市", "parent": "13"},
    "143": {"name": "六安市", "parent": "13"},
    "144": {"name": "亳州市", "parent": "13"},
    "145": {"name": "池州市", "parent": "13"},
    "146": {"name": "宣城市", "parent": "13"},
    "147": {"name": "福州市", "parent": "14"},
    "148": {"name": "厦门市", "parent": "14"},
    "149": {"name": "莆田市", "parent": "14"},
    "150": {"name": "三明市", "parent": "14"},
    "151": {"name": "泉州市", "parent": "14"},
    "152": {"name": "漳州市", "parent": "14"},
    "153": {"name": "南平市", "parent": "14"},
    "154": {"name": "龙岩市", "parent": "14"},
    "155": {"name": "宁德市", "parent": "14"},
    "156": {"name": "南昌市", "parent": "15"},
    "157": {"name": "景德镇市", "parent": "15"},
    "158": {"name": "萍乡市", "parent": "15"},
    "159": {"name": "九江市", "parent": "15"},
    "160": {"name": "新余市", "parent": "15"},
    "161": {"name": "鹰潭市", "parent": "15"},
    "162": {"name": "赣州市", "parent": "15"},
    "163": {"name": "吉安市", "parent": "15"},
    "164": {"name": "宜春市", "parent": "15"},
    "165": {"name": "抚州市", "parent": "15"},
    "166": {"name": "上饶市", "parent": "15"},
    "167": {"name": "济南市", "parent": "16"},
    "168": {"name": "青岛市", "parent": "16"},
    "169": {"name": "淄博市", "parent": "16"},
    "170": {"name": "枣庄市", "parent": "16"},
    "171": {"name": "东营市", "parent": "16"},
    "172": {"name": "烟台市", "parent": "16"},
    "173": {"name": "潍坊市", "parent": "16"},
    "174": {"name": "济宁市", "parent": "16"},
    "175": {"name": "泰安市", "parent": "16"},
    "176": {"name": "威海市", "parent": "16"},
    "177": {"name": "日照市", "parent": "16"},
    "179": {"name": "临沂市", "parent": "16"},
    "180": {"name": "德州市", "parent": "16"},
    "181": {"name": "聊城市", "parent": "16"},
    "182": {"name": "滨州市", "parent": "16"},
    "183": {"name": "菏泽市", "parent": "16"},
    "184": {"name": "郑州市", "parent": "17"},
    "185": {"name": "开封市", "parent": "17"},
    "186": {"name": "洛阳市", "parent": "17"},
    "187": {"name": "平顶山市", "parent": "17"},
    "188": {"name": "安阳市", "parent": "17"},
    "189": {"name": "鹤壁市", "parent": "17"},
    "190": {"name": "新乡市", "parent": "17"},
    "191": {"name": "焦作市", "parent": "17"},
    "192": {"name": "濮阳市", "parent": "17"},
    "193": {"name": "许昌市", "parent": "17"},
    "194": {"name": "漯河市", "parent": "17"},
    "195": {"name": "三门峡市", "parent": "17"},
    "196": {"name": "南阳市", "parent": "17"},
    "197": {"name": "商丘市", "parent": "17"},
    "198": {"name": "信阳市", "parent": "17"},
    "199": {"name": "周口市", "parent": "17"},
    "200": {"name": "驻马店市", "parent": "17"},
    "201": {"name": "武汉市", "parent": "18"},
    "202": {"name": "黄石市", "parent": "18"},
    "203": {"name": "十堰市", "parent": "18"},
    "204": {"name": "宜昌市", "parent": "18"},
    "205": {"name": "襄阳市", "parent": "18"},
    "206": {"name": "鄂州市", "parent": "18"},
    "207": {"name": "荆门市", "parent": "18"},
    "208": {"name": "孝感市", "parent": "18"},
    "209": {"name": "荆州市", "parent": "18"},
    "210": {"name": "黄冈市", "parent": "18"},
    "211": {"name": "咸宁市", "parent": "18"},
    "212": {"name": "随州市", "parent": "18"},
    "213": {"name": "恩施土家族苗族自治州", "parent": "18"},
    "215": {"name": "长沙市", "parent": "19"},
    "216": {"name": "株洲市", "parent": "19"},
    "217": {"name": "湘潭市", "parent": "19"},
    "218": {"name": "衡阳市", "parent": "19"},
    "219": {"name": "邵阳市", "parent": "19"},
    "220": {"name": "岳阳市", "parent": "19"},
    "221": {"name": "常德市", "parent": "19"},
    "222": {"name": "张家界市", "parent": "19"},
    "223": {"name": "益阳市", "parent": "19"},
    "224": {"name": "郴州市", "parent": "19"},
    "225": {"name": "永州市", "parent": "19"},
    "226": {"name": "怀化市", "parent": "19"},
    "227": {"name": "娄底市", "parent": "19"},
    "228": {"name": "湘西土家族苗族自治州", "parent": "19"},
    "229": {"name": "广州市", "parent": "20"},
    "230": {"name": "韶关市", "parent": "20"},
    "231": {"name": "深圳市", "parent": "20"},
    "232": {"name": "珠海市", "parent": "20"},
    "233": {"name": "汕头市", "parent": "20"},
    "234": {"name": "佛山市", "parent": "20"},
    "235": {"name": "江门市", "parent": "20"},
    "236": {"name": "湛江市", "parent": "20"},
    "237": {"name": "茂名市", "parent": "20"},
    "238": {"name": "肇庆市", "parent": "20"},
    "239": {"name": "惠州市", "parent": "20"},
    "240": {"name": "梅州市", "parent": "20"},
    "241": {"name": "汕尾市", "parent": "20"},
    "242": {"name": "河源市", "parent": "20"},
    "243": {"name": "阳江市", "parent": "20"},
    "244": {"name": "清远市", "parent": "20"},
    "245": {"name": "东莞市", "parent": "20"},
    "246": {"name": "中山市", "parent": "20"},
    "247": {"name": "潮州市", "parent": "20"},
    "248": {"name": "揭阳市", "parent": "20"},
    "249": {"name": "云浮市", "parent": "20"},
    "250": {"name": "南宁市", "parent": "21"},
    "251": {"name": "柳州市", "parent": "21"},
    "252": {"name": "桂林市", "parent": "21"},
    "253": {"name": "梧州市", "parent": "21"},
    "254": {"name": "北海市", "parent": "21"},
    "255": {"name": "防城港市", "parent": "21"},
    "256": {"name": "钦州市", "parent": "21"},
    "257": {"name": "贵港市", "parent": "21"},
    "258": {"name": "玉林市", "parent": "21"},
    "259": {"name": "百色市", "parent": "21"},
    "260": {"name": "贺州市", "parent": "21"},
    "261": {"name": "河池市", "parent": "21"},
    "262": {"name": "来宾市", "parent": "21"},
    "263": {"name": "崇左市", "parent": "21"},
    "264": {"name": "海口市", "parent": "22"},
    "265": {"name": "三亚市", "parent": "22"},
    "267": {"name": "重庆市", "parent": "23"},
    "268": {"name": "成都市", "parent": "24"},
    "269": {"name": "自贡市", "parent": "24"},
    "270": {"name": "攀枝花市", "parent": "24"},
    "271": {"name": "泸州市", "parent": "24"},
    "272": {"name": "德阳市", "parent": "24"},
    "273": {"name": "绵阳市", "parent": "24"},
    "274": {"name": "广元市", "parent": "24"},
    "275": {"name": "遂宁市", "parent": "24"},
    "276": {"name": "内江市", "parent": "24"},
    "277": {"name": "乐山市", "parent": "24"},
    "278": {"name": "南充市", "parent": "24"},
    "279": {"name": "眉山市", "parent": "24"},
    "280": {"name": "宜宾市", "parent": "24"},
    "281": {"name": "广安市", "parent": "24"},
    "282": {"name": "达州市", "parent": "24"},
    "283": {"name": "雅安市", "parent": "24"},
    "284": {"name": "巴中市", "parent": "24"},
    "285": {"name": "资阳市", "parent": "24"},
    "286": {"name": "阿坝藏族羌族自治州", "parent": "24"},
    "287": {"name": "甘孜藏族自治州", "parent": "24"},
    "288": {"name": "凉山彝族自治州", "parent": "24"},
    "289": {"name": "贵阳市", "parent": "25"},
    "290": {"name": "六盘水市", "parent": "25"},
    "291": {"name": "遵义市", "parent": "25"},
    "292": {"name": "安顺市", "parent": "25"},
    "293": {"name": "铜仁市", "parent": "25"},
    "294": {"name": "黔西南布依族苗族自治州", "parent": "25"},
    "295": {"name": "毕节市", "parent": "25"},
    "296": {"name": "黔东南苗族侗族自治州", "parent": "25"},
    "297": {"name": "黔南布依族苗族自治州", "parent": "25"},
    "298": {"name": "昆明市", "parent": "26"},
    "299": {"name": "曲靖市", "parent": "26"},
    "300": {"name": "玉溪市", "parent": "26"},
    "301": {"name": "保山市", "parent": "26"},
    "302": {"name": "昭通市", "parent": "26"},
    "303": {"name": "丽江市", "parent": "26"},
    "304": {"name": "普洱市", "parent": "26"},
    "305": {"name": "临沧市", "parent": "26"},
    "306": {"name": "楚雄彝族自治州", "parent": "26"},
    "307": {"name": "红河哈尼族彝族自治州", "parent": "26"},
    "308": {"name": "文山壮族苗族自治州", "parent": "26"},
    "309": {"name": "西双版纳傣族自治州", "parent": "26"},
    "310": {"name": "大理白族自治州", "parent": "26"},
    "311": {"name": "德宏傣族景颇族自治州", "parent": "26"},
    "312": {"name": "怒江傈僳族自治州", "parent": "26"},
    "313": {"name": "迪庆藏族自治州", "parent": "26"},
    "314": {"name": "拉萨市", "parent": "27"},
    "315": {"name": "昌都市", "parent": "27"},
    "316": {"name": "山南市", "parent": "27"},
    "317": {"name": "日喀则市", "parent": "27"},
    "318": {"name": "那曲市", "parent": "27"},
    "319": {"name": "阿里地区", "parent": "27"},
    "320": {"name": "林芝市", "parent": "27"},
    "321": {"name": "西安市", "parent": "28"},
    "322": {"name": "铜川市", "parent": "28"},
    "323": {"name": "宝鸡市", "parent": "28"},
    "324": {"name": "咸阳市", "parent": "28"},
    "325": {"name": "渭南市", "parent": "28"},
    "326": {"name": "延安市", "parent": "28"},
    "327": {"name": "汉中市", "parent": "28"},
    "328": {"name": "榆林市", "parent": "28"},
    "329": {"name": "安康市", "parent": "28"},
    "330": {"name": "商洛市", "parent": "28"},
    "331": {"name": "兰州市", "parent": "29"},
    "332": {"name": "嘉峪关市", "parent": "29"},
    "333": {"name": "金昌市", "parent": "29"},
    "334": {"name": "白银市", "parent": "29"},
    "335": {"name": "天水市", "parent": "29"},
    "336": {"name": "武威市", "parent": "29"},
    "337": {"name": "张掖市", "parent": "29"},
    "338": {"name": "平凉市", "parent": "29"},
    "339": {"name": "酒泉市", "parent": "29"},
    "340": {"name": "庆阳市", "parent": "29"},
    "341": {"name": "定西市", "parent": "29"},
    "342": {"name": "陇南市", "parent": "29"},
    "343": {"name": "临夏回族自治州", "parent": "29"},
    "344": {"name": "甘南藏族自治州", "parent": "29"},
    "345": {"name": "西宁市", "parent": "30"},
    "346": {"name": "海东市", "parent": "30"},
    "347": {"name": "海北藏族自治州", "parent": "30"},
    "348": {"name": "黄南藏族自治州", "parent": "30"},
    "349": {"name": "海南藏族自治州", "parent": "30"},
    "350": {"name": "果洛藏族自治州", "parent": "30"},
    "351": {"name": "玉树藏族自治州", "parent": "30"},
    "352": {"name": "海西蒙古族藏族自治州", "parent": "30"},
    "353": {"name": "银川市", "parent": "31"},
    "354": {"name": "石嘴山市", "parent": "31"},
    "355": {"name": "吴忠市", "parent": "31"},
    "356": {"name": "固原市", "parent": "31"},
    "357": {"name": "中卫市", "parent": "31"},
    "358": {"name": "乌鲁木齐市", "parent": "32"},
    "359": {"name": "克拉玛依市", "parent": "32"},
    "360": {"name": "吐鲁番市", "parent": "32"},
    "361": {"name": "哈密市", "parent": "32"},
    "362": {"name": "昌吉回族自治州", "parent": "32"},
    "363": {"name": "博尔塔拉蒙古自治州", "parent": "32"},
    "364": {"name": "巴音郭楞蒙古自治州", "parent": "32"},
    "365": {"name": "阿克苏地区", "parent": "32"},
    "366": {"name": "克孜勒苏柯尔克孜自治州", "parent": "32"},
    "367": {"name": "喀什地区", "parent": "32"},
    "368": {"name": "和田地区", "parent": "32"},
    "369": {"name": "伊犁哈萨克自治州", "parent": "32"},
    "370": {"name": "塔城地区", "parent": "32"},
    "371": {"name": "阿勒泰地区", "parent": "32"},
    "372": {"name": "新疆省直辖行政单位", "parent": "32"},
    "373": {"name": "可克达拉市", "parent": "32"},
    "374": {"name": "昆玉市", "parent": "32"},
    "375": {"name": "胡杨河市", "parent": "32"},
    "376": {"name": "双河市", "parent": "32"},
    "3560": {"name": "北票市", "parent": "7"},
    "3615": {"name": "高州市", "parent": "20"},
    "3651": {"name": "济源市", "parent": "17"},
    "3662": {"name": "胶南市", "parent": "16"},
    "3683": {"name": "老河口市", "parent": "18"},
    "3758": {"name": "沙河市", "parent": "4"},
    "3822": {"name": "宜城市", "parent": "18"},
    "3842": {"name": "枣阳市", "parent": "18"},
    "3850": {"name": "肇东市", "parent": "9"},
    "3905": {"name": "澳门", "parent": "1"},
    "3906": {"name": "澳门", "parent": "3905"},
    "3907": {"name": "香港", "parent": "1"},
    "3908": {"name": "香港", "parent": "3907"},
    "3947": {"name": "仙桃市", "parent": "18"},
    "3954": {"name": "台湾", "parent": "1"},
    "3955": {"name": "台湾", "parent": "3954"},
    "3956": {"name": "海外", "parent": "1"},
    "3957": {"name": "海外", "parent": "3956"},
    "3958": {"name": "美国", "parent": "3956"},
    "3959": {"name": "加拿大", "parent": "3956"},
    "3961": {"name": "日本", "parent": "3956"},
    "3962": {"name": "韩国", "parent": "3956"},
    "3963": {"name": "德国", "parent": "3956"},
    "3964": {"name": "英国", "parent": "3956"},
    "3965": {"name": "意大利", "parent": "3956"},
    "3966": {"name": "西班牙", "parent": "3956"},
    "3967": {"name": "法国", "parent": "3956"},
    "3968": {"name": "澳大利亚", "parent": "3956"},
    "3969": {"name": "东城区", "parent": "2"},
    "3970": {"name": "西城区", "parent": "2"},
    "3971": {"name": "崇文区", "parent": "2"},
    "3972": {"name": "宣武区", "parent": "2"},
    "3973": {"name": "朝阳区", "parent": "2"},
    "3974": {"name": "海淀区", "parent": "2"},
    "3975": {"name": "丰台区", "parent": "2"},
    "3976": {"name": "石景山区", "parent": "2"},
    "3977": {"name": "门头沟区", "parent": "2"},
    "3978": {"name": "房山区", "parent": "2"},
    "3979": {"name": "通州区", "parent": "2"},
    "3980": {"name": "顺义区", "parent": "2"},
    "3981": {"name": "昌平区", "parent": "2"},
    "3982": {"name": "大兴区", "parent": "2"},
    "3983": {"name": "平谷区", "parent": "2"},
    "3984": {"name": "怀柔区", "parent": "2"},
    "3985": {"name": "密云区", "parent": "2"},
    "3986": {"name": "延庆区", "parent": "2"},
    "3987": {"name": "黄浦区", "parent": "10"},
    "3988": {"name": "徐汇区", "parent": "10"},
    "3989": {"name": "长宁区", "parent": "10"},
    "3990": {"name": "静安区", "parent": "10"},
    "3991": {"name": "普陀区", "parent": "10"},
    "3992": {"name": "闸北区", "parent": "10"},
    "3993": {"name": "虹口区", "parent": "10"},
    "3994": {"name": "杨浦区", "parent": "10"},
    "3995": {"name": "宝山区", "parent": "10"},
    "3996": {"name": "闵行区", "parent": "10"},
    "3997": {"name": "嘉定区", "parent": "10"},
    "3998": {"name": "浦东新区", "parent": "10"},
    "3999": {"name": "松江区", "parent": "10"},
    "4000": {"name": "金山区", "parent": "10"},
    "4001": {"name": "青浦区", "parent": "10"},
    "4002": {"name": "奉贤区", "parent": "10"},
    "4003": {"name": "崇明区", "parent": "10"},
    "4004": {"name": "和平区", "parent": "3"},
    "4005": {"name": "河东区", "parent": "3"},
    "4006": {"name": "河西区", "parent": "3"},
    "4007": {"name": "南开区", "parent": "3"},
    "4008": {"name": "红桥区", "parent": "3"},
    "4009": {"name": "河北区", "parent": "3"},
    "4010": {"name": "滨海新区", "parent": "3"},
    "4011": {"name": "东丽区", "parent": "3"},
    "4012": {"name": "西青区", "parent": "3"},
    "4013": {"name": "北辰区", "parent": "3"},
    "4014": {"name": "津南区", "parent": "3"},
    "4015": {"name": "武清区", "parent": "3"},
    "4016": {"name": "宝坻区", "parent": "3"},
    "4017": {"name": "静海区", "parent": "3"},
    "4018": {"name": "宁河区", "parent": "3"},
    "4019": {"name": "蓟州区", "parent": "3"},
    "4020": {"name": "渝中区", "parent": "23"},
    "4021": {"name": "江北区", "parent": "23"},
    "4022": {"name": "南岸区", "parent": "23"},
    "4023": {"name": "沙坪坝区", "parent": "23"},
    "4024": {"name": "九龙坡区", "parent": "23"},
    "4025": {"name": "大渡口区", "parent": "23"},
    "4026": {"name": "渝北区", "parent": "23"},
    "4027": {"name": "巴南区", "parent": "23"},
    "4028": {"name": "北碚区", "parent": "23"},
    "4029": {"name": "万州区", "parent": "23"},
    "4030": {"name": "黔江区", "parent": "23"},
    "4031": {"name": "永川区", "parent": "23"},
    "4032": {"name": "涪陵区", "parent": "23"},
    "4033": {"name": "江津区", "parent": "23"},
    "4034": {"name": "合川区", "parent": "23"},
    "4035": {"name": "双桥区", "parent": "23"},
    "4036": {"name": "万盛区", "parent": "23"},
    "4037": {"name": "荣昌区", "parent": "23"},
    "4038": {"name": "大足区", "parent": "23"},
    "4039": {"name": "璧山区", "parent": "23"},
    "4040": {"name": "铜梁区", "parent": "23"},
    "4041": {"name": "潼南区", "parent": "23"},
    "4042": {"name": "綦江区", "parent": "23"},
    "4043": {"name": "忠县", "parent": "23"},
    "4044": {"name": "开州区", "parent": "23"},
    "4045": {"name": "云阳县", "parent": "23"},
    "4046": {"name": "梁平区", "parent": "23"},
    "4047": {"name": "垫江县", "parent": "23"},
    "4048": {"name": "丰都县", "parent": "23"},
    "4049": {"name": "奉节县", "parent": "23"},
    "4050": {"name": "巫山县", "parent": "23"},
    "4051": {"name": "巫溪县", "parent": "23"},
    "4052": {"name": "城口县", "parent": "23"},
    "4053": {"name": "武隆区", "parent": "23"},
    "4054": {"name": "石柱土家族自治县", "parent": "23"},
    "4055": {"name": "秀山土家族苗族自治县", "parent": "23"},
    "4056": {"name": "酉阳土家族苗族自治县", "parent": "23"},
    "4057": {"name": "彭水苗族土家族自治县", "parent": "23"},
    "4058": {"name": "潜江市", "parent": "18"},
    "4059": {"name": "三沙市", "parent": "22"},
    "4060": {"name": "石河子市", "parent": "32"},
    "4061": {"name": "阿拉尔市", "parent": "32"},
    "4062": {"name": "图木舒克市", "parent": "32"},
    "4063": {"name": "五家渠市", "parent": "32"},
    "4064": {"name": "北屯市", "parent": "32"},
    "4065": {"name": "铁门关市", "parent": "32"},
    "4066": {"name": "儋州市", "parent": "22"},
    "4067": {"name": "五指山市", "parent": "22"},
    "4068": {"name": "文昌市", "parent": "22"},
    "4069": {"name": "琼海市", "parent": "22"},
    "4070": {"name": "万宁市", "parent": "22"},
    "4072": {"name": "定安县", "parent": "22"},
    "4073": {"name": "屯昌县", "parent": "22"},
    "4074": {"name": "澄迈县", "parent": "22"},
    "4075": {"name": "临高县", "parent": "22"},
    "4076": {"name": "琼中黎族苗族自治县", "parent": "22"},
    "4077": {"name": "保亭黎族苗族自治县", "parent": "22"},
    "4078": {"name": "白沙黎族自治县", "parent": "22"},
    "4079": {"name": "昌江黎族自治县", "parent": "22"},
    "4080": {"name": "乐东黎族自治县", "parent": "22"},
    "4081": {"name": "陵水黎族自治县", "parent": "22"},
    "4082": {"name": "马来西亚", "parent": "3956"},
    "6047": {"name": "长寿区", "parent": "23"},
    "6857": {"name": "阿富汗", "parent": "3956"},
    "6858": {"name": "阿尔巴尼亚", "parent": "3956"},
    "6859": {"name": "阿尔及利亚", "parent": "3956"},
    "6860": {"name": "美属萨摩亚", "parent": "3956"},
    "6861": {"name": "安道尔", "parent": "3956"},
    "6862": {"name": "安哥拉", "parent": "3956"},
    "6863": {"name": "安圭拉", "parent": "3956"},
    "6864": {"name": "南极洲", "parent": "3956"},
    "6865": {"name": "安提瓜和巴布达", "parent": "3956"},
    "6866": {"name": "阿根廷", "parent": "3956"},
    "6867": {"name": "亚美尼亚", "parent": "3956"},
    "6869": {"name": "奥地利", "parent": "3956"},
    "6870": {"name": "阿塞拜疆", "parent": "3956"},
    "6871": {"name": "巴哈马", "parent": "3956"},
    "6872": {"name": "巴林", "parent": "3956"},
    "6873": {"name": "孟加拉国", "parent": "3956"},
    "6874": {"name": "巴巴多斯", "parent": "3956"},
    "6875": {"name": "白俄罗斯", "parent": "3956"},
    "6876": {"name": "比利时", "parent": "3956"},
    "6877": {"name": "伯利兹", "parent": "3956"},
    "6878": {"name": "贝宁", "parent": "3956"},
    "6879": {"name": "百慕大", "parent": "3956"},
    "6880": {"name": "不丹", "parent": "3956"},
    "6881": {"name": "玻利维亚", "parent": "3956"},
    "6882": {"name": "波黑", "parent": "3956"},
    "6883": {"name": "博茨瓦纳", "parent": "3956"},
    "6884": {"name": "布维岛", "parent": "3956"},
    "6885": {"name": "巴西", "parent": "3956"},
    "6886": {"name": "英属印度洋领土", "parent": "3956"},
    "6887": {"name": "文莱", "parent": "3956"},
    "6888": {"name": "保加利亚", "parent": "3956"},
    "6889": {"name": "布基纳法索", "parent": "3956"},
    "6890": {"name": "布隆迪", "parent": "3956"},
    "6891": {"name": "柬埔寨", "parent": "3956"},
    "6892": {"name": "喀麦隆", "parent": "3956"},
    "6893": {"name": "佛得角", "parent": "3956"},
    "6894": {"name": "开曼群岛", "parent": "3956"},
    "6895": {"name": "中非", "parent": "3956"},
    "6896": {"name": "乍得", "parent": "3956"},
    "6897": {"name": "智利", "parent": "3956"},
    "6898": {"name": "圣诞岛", "parent": "3956"},
    "6899": {"name": "科科斯（基林）群岛", "parent": "3956"},
    "6900": {"name": "哥伦比亚", "parent": "3956"},
    "6901": {"name": "科摩罗", "parent": "3956"},
    "6902": {"name": "刚果（布）", "parent": "3956"},
    "6903": {"name": "刚果（金）", "parent": "3956"},
    "6904": {"name": "库克群岛", "parent": "3956"},
    "6905": {"name": "哥斯达黎加", "parent": "3956"},
    "6906": {"name": "科特迪瓦", "parent": "3956"},
    "6907": {"name": "克罗地亚", "parent": "3956"},
    "6908": {"name": "古巴", "parent": "3956"},
    "6909": {"name": "塞浦路斯", "parent": "3956"},
    "6910": {"name": "捷克", "parent": "3956"},
    "6911": {"name": "丹麦", "parent": "3956"},
    "6912": {"name": "吉布提", "parent": "3956"},
    "6913": {"name": "多米尼克", "parent": "3956"},
    "6914": {"name": "多米尼加共和国", "parent": "3956"},
    "6915": {"name": "东帝汶", "parent": "3956"},
    "6916": {"name": "厄瓜多尔", "parent": "3956"},
    "6917": {"name": "埃及", "parent": "3956"},
    "6918": {"name": "萨尔瓦多", "parent": "3956"},
    "6919": {"name": "赤道几内亚", "parent": "3956"},
    "6920": {"name": "厄立特里亚", "parent": "3956"},
    "6921": {"name": "爱沙尼亚", "parent": "3956"},
    "6922": {"name": "埃塞俄比亚", "parent": "3956"},
    "6923": {"name": "福克兰群岛（马尔维纳斯）", "parent": "3956"},
    "6924": {"name": "法罗群岛", "parent": "3956"},
    "6925": {"name": "斐济", "parent": "3956"},
    "6926": {"name": "芬兰", "parent": "3956"},
    "6927": {"name": "法属圭亚那", "parent": "3956"},
    "6928": {"name": "法属波利尼西亚", "parent": "3956"},
    "6929": {"name": "法属南部领土", "parent": "3956"},
    "6930": {"name": "加蓬", "parent": "3956"},
    "6931": {"name": "冈比亚", "parent": "3956"},
    "6932": {"name": "格鲁吉亚", "parent": "3956"},
    "6933": {"name": "加纳", "parent": "3956"},
    "6934": {"name": "直布罗陀", "parent": "3956"},
    "6935": {"name": "希腊", "parent": "3956"},
    "6936": {"name": "格陵兰", "parent": "3956"},
    "6937": {"name": "格林纳达", "parent": "3956"},
    "6938": {"name": "瓜德罗普", "parent": "3956"},
    "6939": {"name": "关岛", "parent": "3956"},
    "6940": {"name": "危地马拉", "parent": "3956"},
    "6941": {"name": "几内亚", "parent": "3956"},
    "6942": {"name": "几内亚比绍", "parent": "3956"},
    "6943": {"name": "圭亚那", "parent": "3956"},
    "6944": {"name": "海地", "parent": "3956"},
    "6945": {"name": "赫德岛和麦克唐纳岛", "parent": "3956"},
    "6946": {"name": "洪都拉斯", "parent": "3956"},
    "6947": {"name": "匈牙利", "parent": "3956"},
    "6948": {"name": "冰岛", "parent": "3956"},
    "6949": {"name": "印度", "parent": "3956"},
    "6950": {"name": "印度尼西亚", "parent": "3956"},
    "6951": {"name": "伊朗", "parent": "3956"},
    "6952": {"name": "伊拉克", "parent": "3956"},
    "6953": {"name": "爱尔兰", "parent": "3956"},
    "6954": {"name": "以色列", "parent": "3956"},
    "6955": {"name": "牙买加", "parent": "3956"},
    "6956": {"name": "约旦", "parent": "3956"},
    "6957": {"name": "哈萨克斯坦", "parent": "3956"},
    "6958": {"name": "肯尼亚", "parent": "3956"},
    "6959": {"name": "基里巴斯", "parent": "3956"},
    "6960": {"name": "朝鲜", "parent": "3956"},
    "6961": {"name": "科威特", "parent": "3956"},
    "6962": {"name": "吉尔吉斯斯坦", "parent": "3956"},
    "6963": {"name": "老挝", "parent": "3956"},
    "6964": {"name": "拉脱维亚", "parent": "3956"},
    "6965": {"name": "黎巴嫩", "parent": "3956"},
    "6966": {"name": "莱索托", "parent": "3956"},
    "6967": {"name": "利比里亚", "parent": "3956"},
    "6968": {"name": "利比亚", "parent": "3956"},
    "6969": {"name": "列支敦士登", "parent": "3956"},
    "6970": {"name": "立陶宛", "parent": "3956"},
    "6971": {"name": "卢森堡", "parent": "3956"},
    "6972": {"name": "前南马其顿", "parent": "3956"},
    "6973": {"name": "马达加斯加", "parent": "3956"},
    "6974": {"name": "马拉维", "parent": "3956"},
    "6975": {"name": "马尔代夫", "parent": "3956"},
    "6976": {"name": "马里", "parent": "3956"},
    "6977": {"name": "马耳他", "parent": "3956"},
    "6978": {"name": "马绍尔群岛", "parent": "3956"},
    "6979": {"name": "马提尼克", "parent": "3956"},
    "6980": {"name": "毛里塔尼亚", "parent": "3956"},
    "6981": {"name": "毛里求斯", "parent": "3956"},
    "6982": {"name": "马约特", "parent": "3956"},
    "6983": {"name": "墨西哥", "parent": "3956"},
    "6984": {"name": "密克罗尼西亚联邦", "parent": "3956"},
    "6985": {"name": "摩尔多瓦", "parent": "3956"},
    "6986": {"name": "摩纳哥", "parent": "3956"},
    "6987": {"name": "蒙古", "parent": "3956"},
    "6988": {"name": "蒙特塞拉特", "parent": "3956"},
    "6989": {"name": "摩洛哥", "parent": "3956"},
    "6990": {"name": "莫桑比克", "parent": "3956"},
    "6991": {"name": "缅甸", "parent": "3956"},
    "6992": {"name": "纳米比亚", "parent": "3956"},
    "6993": {"name": "瑙鲁", "parent": "3956"},
    "6994": {"name": "尼泊尔", "parent": "3956"},
    "6995": {"name": "荷兰", "parent": "3956"},
    "6996": {"name": "荷属安的列斯", "parent": "3956"},
    "6997": {"name": "新喀里多尼亚", "parent": "3956"},
    "6998": {"name": "新西兰", "parent": "3956"},
    "6999": {"name": "尼加拉瓜", "parent": "3956"},
    "7000": {"name": "尼日尔", "parent": "3956"},
    "7001": {"name": "尼日利亚", "parent": "3956"},
    "7002": {"name": "纽埃", "parent": "3956"},
    "7003": {"name": "诺福克岛", "parent": "3956"},
    "7004": {"name": "北马里亚纳", "parent": "3956"},
    "7005": {"name": "挪威", "parent": "3956"},
    "7006": {"name": "阿曼", "parent": "3956"},
    "7007": {"name": "巴基斯坦", "parent": "3956"},
    "7008": {"name": "帕劳", "parent": "3956"},
    "7009": {"name": "巴勒斯坦", "parent": "3956"},
    "7010": {"name": "巴拿马", "parent": "3956"},
    "7011": {"name": "巴布亚新几内亚", "parent": "3956"},
    "7012": {"name": "巴拉圭", "parent": "3956"},
    "7013": {"name": "秘鲁", "parent": "3956"},
    "7014": {"name": "菲律宾", "parent": "3956"},
    "7015": {"name": "皮特凯恩群岛", "parent": "3956"},
    "7016": {"name": "波兰", "parent": "3956"},
    "7017": {"name": "葡萄牙", "parent": "3956"},
    "7018": {"name": "波多黎各", "parent": "3956"},
    "7019": {"name": "卡塔尔", "parent": "3956"},
    "7020": {"name": "留尼汪", "parent": "3956"},
    "7021": {"name": "罗马尼亚", "parent": "3956"},
    "7022": {"name": "俄罗斯联邦", "parent": "3956"},
    "7023": {"name": "卢旺达", "parent": "3956"},
    "7024": {"name": "圣赫勒拿", "parent": "3956"},
    "7025": {"name": "圣基茨和尼维斯", "parent": "3956"},
    "7026": {"name": "圣卢西亚", "parent": "3956"},
    "7027": {"name": "圣皮埃尔和密克隆", "parent": "3956"},
    "7028": {"name": "圣文森特和格林纳丁斯", "parent": "3956"},
    "7029": {"name": "萨摩亚", "parent": "3956"},
    "7030": {"name": "圣马力诺", "parent": "3956"},
    "7031": {"name": "圣多美和普林西比", "parent": "3956"},
    "7032": {"name": "沙特阿拉伯", "parent": "3956"},
    "7033": {"name": "塞内加尔", "parent": "3956"},
    "7034": {"name": "塞舌尔", "parent": "3956"},
    "7035": {"name": "塞拉利昂", "parent": "3956"},
    "7036": {"name": "新加坡", "parent": "3956"},
    "7037": {"name": "斯洛伐克", "parent": "3956"},
    "7038": {"name": "斯洛文尼亚", "parent": "3956"},
    "7039": {"name": "所罗门群岛", "parent": "3956"},
    "7040": {"name": "索马里", "parent": "3956"},
    "7041": {"name": "南非", "parent": "3956"},
    "7042": {"name": "南乔治亚岛和南桑德韦奇岛", "parent": "3956"},
    "7043": {"name": "斯里兰卡", "parent": "3956"},
    "7044": {"name": "苏丹", "parent": "3956"},
    "7045": {"name": "苏里南", "parent": "3956"},
    "7046": {"name": "斯瓦尔巴群岛", "parent": "3956"},
    "7047": {"name": "斯威士兰", "parent": "3956"},
    "7048": {"name": "瑞典", "parent": "3956"},
    "7049": {"name": "瑞士", "parent": "3956"},
    "7050": {"name": "叙利亚", "parent": "3956"},
    "7051": {"name": "塔吉克斯坦", "parent": "3956"},
    "7052": {"name": "坦桑尼亚", "parent": "3956"},
    "7053": {"name": "泰国", "parent": "3956"},
    "7054": {"name": "多哥", "parent": "3956"},
    "7055": {"name": "托克劳", "parent": "3956"},
    "7056": {"name": "汤加", "parent": "3956"},
    "7057": {"name": "特立尼达和多巴哥", "parent": "3956"},
    "7058": {"name": "突尼斯", "parent": "3956"},
    "7059": {"name": "土耳其", "parent": "3956"},
    "7060": {"name": "土库曼斯坦", "parent": "3956"},
    "7061": {"name": "特克斯科斯群岛", "parent": "3956"},
    "7062": {"name": "图瓦卢", "parent": "3956"},
    "7063": {"name": "乌干达", "parent": "3956"},
    "7064": {"name": "乌克兰", "parent": "3956"},
    "7065": {"name": "阿联酋", "parent": "3956"},
    "7066": {"name": "美国本土外小岛屿", "parent": "3956"},
    "7067": {"name": "乌拉圭", "parent": "3956"},
    "7068": {"name": "乌兹别克斯坦", "parent": "3956"},
    "7069": {"name": "瓦努阿图", "parent": "3956"},
    "7070": {"name": "梵蒂冈", "parent": "3956"},
    "7071": {"name": "委内瑞拉", "parent": "3956"},
    "7072": {"name": "越南", "parent": "3956"},
    "7073": {"name": "英属维尔京群岛", "parent": "3956"},
    "7074": {"name": "美属维尔京群岛", "parent": "3956"},
    "7075": {"name": "瓦利斯和富图纳", "parent": "3956"},
    "7076": {"name": "西撒哈拉", "parent": "3956"},
    "7077": {"name": "也门", "parent": "3956"},
    "7078": {"name": "南斯拉夫", "parent": "3956"},
    "7079": {"name": "赞比亚", "parent": "3956"},
    "7080": {"name": "津巴布韦", "parent": "3956"},
    "7081": {"name": "塞尔维亚", "parent": "3956"},
    "7082": {"name": "雄安新区", "parent": "4"},
    "7084": {"name": "天门市", "parent": "18"},
}

NM_SET = set([v["name"] for _, v in TBL.items()])


def get_names(id):
    if not id or str(id).lower() == "none":
        return []
    id = str(id)
    if not re.match("[0-9]+$", id.strip()):
        return [id]
    nms = []
    d = TBL.get(id)
    if not d:
        return []
    nms.append(d["name"])
    p = get_names(d["parent"])
    if p:
        nms.extend(p)
    return nms



def isName(nm):
    if nm in NM_SET:
        return True
    if nm + "市" in NM_SET:
        return True
    if re.sub(r"(省|(回族|壮族|维吾尔)*自治区)$", "", nm) in NM_SET:
        return True
    return False
