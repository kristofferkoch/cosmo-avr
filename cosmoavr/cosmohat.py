from __future__ import print_function
import cosmospi
        
class CosmoHat(cosmospi.CosmoSpi):
    def version(self):
        return ''.join(chr(x) for x in self.call(0))

    def adcs(self, adcs=[0,1,2,3,4,5,6,7]):
        mask = 0
        for adc in adcs:
            assert adc < 8
            mask |= 1<<adc
        ret = []
        data = self.call(1,[mask])
        assert len(data) == len(adcs)*2
        #print(data)
        for i in adcs:
            ret.append((data[2*i+1]<<8)|data[2*i])
        return ret

    def get_gpios(self):
        data, = self.call(2)
        return data
        