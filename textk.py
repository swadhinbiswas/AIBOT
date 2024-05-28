# from Bot.API.photogen2 import text_to_image 


# text_to_image("create a bright modern abstract flat 3d illustration with gouache shading in the style of Alex Kiesling for a magazine cover, a womans head surrounded by flowers, face immersed in petals, contempt, lotus, magnolias, sunlight enters from the left, pastel colors, fullness, mindfulness, leave empty space on the right, low detail, soft shadows, light and airy, ethereal, dreamy, surreal, whimsical, magical, mystical, spiritual, feminine")


from Bot.API.Geminiapp import geminiapp


x=geminiapp(["Hello",None])


print(x)