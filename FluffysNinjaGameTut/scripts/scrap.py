class anim:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.duration = img_dur
        self.loop = loop

    def copy(self):
        return anim(self.images, self.duration, self.loop)
    
class main:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
        self.duration = 6
        self.loop = True
        self.frame = 0
        self.i = 0

    def update(self):
        while self.loop:
            self.frame = (self.frame + 1) % (self.duration * len(self.nums))
            print(self.get_num())
            self.i += 1
            if self.i == 100:
                self.loop = False
    
    def get_num(self):
        return self.nums[int(self.frame / self.duration)]
    
    def print_nums(self):
        print(self.update())

main().print_nums()