init python:
    class Calender(object):
        def __init__(self, Hours, Hour, Days, Day, Months, Month, WeakDays, MonthDays):
            self.Hours = Hours
            self.Hour = Hour
            self.Days = Days
            self.Day = Day
            self.Months = Months
            self.Month = Month
            self.WeakDays = WeakDays
            self.MonthDays = MonthDays
        
        @property
        def Output(self):
            return self.WeakDays[self.Day] + " " + self.Months[self.Month] + " " + str(self.Days+1) + " " + str(self.Hours).zfill(2) + ":00"
        
        def Add_time(self, Hours):
            self.Hours += Hours
            if self.Hours > 23:
                self.Hours -= 24
                self.Day+= 1
                self.Days += 1
            if self.Day > 6:
                self.Day = 0
            if self.Days > self.MonthDays[self.Month]:
                self.Month +=1
                self.Days = 0
            if self.Month > 11:
                self.Month = 0
    
    class Event(object):
        def __init__(self, Hours, Day, Month, Block, IsActive):
            self.Hours = Hours
            self.Day = Day
            self.Month = Month
            self.Block = Block
            self.IsActive = IsActive
        def DateCheck(self, c):
            if self.Day == c.Day and self.Hours == c.Hours and self.Month == c.Month and self.IsActive:
                return True
            else:
                return False
        def setInactive(self):
            self.IsActive = False
    
    class Items(object):
        def __init__(self, name, val, weight, NoOwned, ID):
            self.name = name
            self.val = val
            self.weight = weight
            self.NoOwned = NoOwned
            self.ID = ID
        def AddItem(self):
            MaxWeight = 50
            CurrentWeight = 0
            for q in INVENTORY:
                CurrentWeight += (q.weight*q.NoOwned)
            if CurrentWeight+self.weight > MaxWeight:
                return
            else:
                self.NoOwned+=1

    EVENTS = []
    INVENTORY = []
    t = 0
    while t < 50:
        EVENTS.append(Event(0, 0, 0, "", False))
        INVENTORY.append(Items("none", 0, 0, 0, t))
        t+=1
