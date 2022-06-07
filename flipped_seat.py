import tweepy

class Flip:
    '''
    These riddings all had their incumbents lose reelection.
    '''
    def __init__(self) -> None:
        self.client = tweepy.Client(bearer_token= 'AAAAAAAAAAAAAAAAAAAAAP%2BhdAEAAAAAmQQeypzMWmPjSrNx0U%2Bv0NQHh%2Fc%3DfsPqIoje91MPrmL2yQftjsjeqyXRa3G2uTzJyKRKbOC4OmKGaQ')
    
    def york_south(self):
        self.ridding = {'OLP':'nadia_guerrera', 'ONDP':'FaisalHassanNDP', 'PCPO':'MichaelFordPC'}
        return self.ridding
    def ys_id(self):
        self.riding = {'OLP':'1362613405', 'ONDP':'266734397', 'PCPO':'1511079939457617923'}
        return self.riding
    
    def beaches(self):
        self.ridding = {'OLP':'marymargaretbey', 'ONDP':'DrKateTO', 'PCPO':'KennedyTCDSB', 'GPO': 'AbhijeetMonet'}
        return self.ridding
    def bb_id(self):
        self.riding = {'OLP':'268410291', 'ONDP':'486788914', 'PCPO':'555220203','GPO': '949131277'}
        return self.riding

    def toronto_centre(self):
        self.ridding = {'OLP':'DavidMorris_TO', 'ONDP':'kristynwongtam', 'PCPO':'JessGoddardPC', 'GPO': 'nicki_ward'}
        return self.ridding
    def tc_id(self):
        self.riding = {'OLP':'557432349', 'ONDP':'20452161', 'PCPO':'1492513756315795463','GPO': '3397502375'}
        return self.riding

    def thunder_bay(self):
        self.ridding = {'ONDP':'Judith_NDP', 'PCPO':'MayorKHolland'}
        return self.ridding
    def tb_id(self):
        self.riding = {'ONDP':'978807879246536704','PCPO':'1121228673779150848'}
        return self.riding

    def kingston(self):
        self.ridding = {'OLP':'tedhsu', 'ONDP':'MaryRitaHolland', 'PCPO':'garybennettpc'}
        return self.ridding
    def king_id(self):
        self.riding = {'OLP':'59084035', 'ONDP':'341876717', 'PCPO':'827180944004091905'}
        return self.riding
    
    def ottawa_west(self):
        self.ridding = {'OLP':'sambhalesar', 'ONDP':'ChandraPasma', 'PCPO':'JR_Ottawa'}
        return self.ridding
    def ow_id(self):
        self.riding = {'OLP':'2800898526', 'ONDP':'984232620975247361', 'PCPO':'1161646903'}
        return self.riding
    
    def prescott(self):
        self.ridding = {'OLP':'ASimardL', 'PCPO':'gpr_pc'}
        return self.ridding
    def gpr_id(self):
        self.riding = {'OLP':'133355510', 'PCPO':'1425171112774807553'}
        return self.riding
    
    def windsor(self):
        self.ridding = {'OLP':'garykaschakwt','ONDP':'hall_grey', 'PCPO':'Andrew_Dowie'}
        return self.ridding
    def wt_id(self):
        self.riding = {'OLP':'1516496462049329159', 'ONDP':'4078948263','PCPO':'411801628'}
        return self.riding
    
    def scarborough(self):
        self.ridding = {'OLP':'mazharshafiq','ONDP':'NeethanShan', 'PCPO':'DavidSmith4PC'}
        return self.ridding
    def sc_id(self):
        self.riding = {'OLP':'16267433', 'ONDP':'29908398','PCPO':'1508859055946838033'}
        return self.riding
    