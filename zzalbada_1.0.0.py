from urllib.request import urlopen
import re
import os

def dc_image_download(gall,start,end):
    dirname = "[{}] {}~{} 이미지".format(gall,start,end)
    if not os.path.isdir("./" + dirname + "/"):
        os.mkdir("./" + dirname + "/")

    for doc_no in range(start,end+1):
        html_read = urlopen('http://gall.dcinside.com/board/view/?id='+gall+'&no='+str(doc_no)).read().decode('utf-8','ignore')
        img_url_list=re.findall("<li class=\"icon_pic\"><a href=\".*?[<]",html_read)

        print("\n◎ 글 번호 : {} ({} / {})".format(doc_no,doc_no+1-start,end+1-start))
        for img_url in img_url_list:
            img_id=img_url[img_url.find("?id=")+len("?id="):img_url.rfind("\">")]
            img_name=img_url[img_url.rfind("\">")+len("\">"):-1]
            if img_name.find(".") == -1:
                img_name = img_name+".jpg"
            
            try:
                open(dirname+"/"+img_name,mode='wb').write(urlopen('http://image.dcinside.com/viewimage.php?id='+img_id).read())
            except:
                pass
            print("\t[다운 완료] {}".format(img_name))
    print("\n모든 다운로드가 완료 되었습니다.")


print("\n이 프로그램의 저작권은 산타보이(santaboyv@gmail.com)에게 있습니다.")
print("무단 복제 및 배포를 금합니다. (디시인사이드 이미지 다운로더 ver 1.0.0)\n")
print("---------------------")
gall = input("갤 이름 : ")
start = int(input("시작 번호 : "))
end = int(input("끝 번호 : "))
print("---------------------")
dc_image_download(gall,start,end)
input()
