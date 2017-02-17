''' Fast genetators by Phonphey '''

#!/usr/bin/env python3

#- * -coding: utf - 8 - * -

import random
import header

class Gen():
    ''' Класс генераторов'''

    def rand_map_gen(self):
        
        gen_map = list()

        for i in range(0, 150, 1):

            k = 0
            tumb = True
            tmp_str = ""

            while tumb:

                if k == 0:
                    tmp_str += "|"

                lucky = random.randint(1, 100)

                if lucky <= 50:
                    tmp_str += random.choice(header)

                

if __name__ == "__main__":
    TMP_CLASS = Gen()
    TMP = TMP_CLASS.rand_map_gen()
