from fontTools import subset

options = subset.Options() # dir(options)
font = subset.load_font('shuibo.ttf', options)
subsetter = subset.Subsetter(options)
subsetter.populate(text = 'Google')
subsetter.subset(font)
options.flavor = 'woff'
subset.save_font(font, 'font.woff', options)