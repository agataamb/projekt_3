# -*- coding: utf-8 -*-

from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from geopy.distance import vincenty
from kivy.properties import NumericProperty 
class Form(BoxLayout):
    score = NumericProperty(1)
    score = 0
            
    def draw_marker(self):
        
        self.list_of_points = [
                ['paris.jpg', 49, 3],
                ['sydney.jpg', -33, 151],
                ['rio.jpg', -22, -43],
                ['nyc.jpg', 40, -74],
                ['tajmahal.jpg', 27, 78],
                ['burji.jpg', 25, 55],
                ['barcelona.jpg', 41, 2],
                ['rzym.jpg', 41, 12],
                ['bigben.jpg', 51, -0],
                ['pkin.jpg', 52, 21]
                ]
        
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        self.latitude = self.my_map.lat
        self.longtitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longtitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = "{:.5f}".format(self.latitude)
        self.search_long.text = "{:.5f}".format(self.longtitude)
        
        
    def check_points(self):
        print(self.list_of_points[0][0])
        #if self.my_image.source == self.list_of_points[0][0]:
            #print('wynik')
        self.p1 = (self.latitude,self.longtitude)
        p2 = (self.list_of_points[0][1], self.list_of_points[0][2])
        self.dist = vincenty(self.p1,p2).meters
        print(self.dist)
        self.dista = "{:.1f}".format(self.dist)
        self.ids['dist'].text = str(self.dista)+'m'
        

        if float(self.dista) < 10000:
            self.score += 1 
            self.ids['wynik'].text = str(self.score)
    def next_img(self):
        self.list_of_points = [0]+1
        
class MapViewApp(App):
    pass

MapViewApp().run()