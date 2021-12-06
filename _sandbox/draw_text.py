import barchart_manager
import graphic

bsm = barchart_manager.BarChartManager(500, 400)
graphic = graphic.Graphic()

fontsize = 70
bottom_y = 100
top_y = bottom_y + fontsize

graphic.draw_line(0, top_y, 500, top_y, linecolor='red')
graphic.draw_text(0, bottom_y, 'Ripple', fontsize=fontsize, fonttype='bold')
graphic.draw_line(0, bottom_y, 500, bottom_y, linecolor='blue')

bsm.screen.mainloop()
