import simple_image_download.simple_image_download as simp
import Script
def main():
    script, scriptList = Script.main()
    sList = scriptList.split(",")
    print(sList)
    
    my_downloader = simp.Downloader()

    for topic in sList:
        try:
            my_downloader.download(topic, limit=3)
            my_downloader.extensions = '.jpg'
        except:
            pass
    return(script, sList)
