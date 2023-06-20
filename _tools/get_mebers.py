import copy

t='''

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/ChenHao.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Hao Chen</P>
<P class="STYLE30">Hao Chen received his B.S degree in School of Astronautics, Beihang University in 2017. He is a bachelor-straight-to-doctorate in the Image Processing Center, School of Astronautics, Beihang University. His research interests include remote sensing image classification and pattern recognition. 
<P class="STYLE30"><A href="mailto:justchenhao@buaa.edu.cn">justchenhao@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/LiWenyuan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Wenyuan Li</P>
<P class="STYLE30">Wenyuan Li received the B.S. degree from HuaDian University, Beijing, China, in 2017. He is currently working toward the Phd degree in the Image Processing Center, School of Astronautics, Beihang University.His research interests include deep learning and pattern recognition.
<P class="STYLE30"><A href="mailto:liwenyuan@buaa.edu.cn">liwenyuan@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/zaoyifan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Yifan Zao</P>
<P class="STYLE30">Yifan Zao received the B.S. degree in the School of Astronautics, Beihang University, Beijing, China, in 2018. He is currently working toward the Phd degree in the Image Processing Center, School of Astronautics, Beihang University. 
His research interests include deep learning and pattern recognition.
<p class="STYLE30"><A href="mailto:zaoyifan@buaa.edu.cn">zaoyifan@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/liuliqin.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Liqin Liu</P>
<P class="STYLE30">LiQin Liu received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2018. She is currently working toward the Phd degree in the Image Processing Center, School of Astronautics, Beihang University.
Her research interests include hyperspectral image classification and deep learning.
<P class="STYLE30"><A href="mailto:liuliqin@buaa.edu.cn">liuliqin@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/YangJiaJun.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Jiajun Yang</P>
<P class="STYLE30">Jiajun Yang received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2016, and received the M.S. degree from China Academy of Space Technology in 2020. He is currently working toward the Phd degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include deep learning and pattern recognition.
<p class="STYLE30"><A href="mailto:yangjiajun@buaa.edu.cn">yangjiajun@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/QiZiPeng.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Zipeng Qi</P>
<P class="STYLE30">He obtained his bachelor's degree from Hebei University of technology in 2018, and now he is studying for a doctor's degree in the image center of the Beihang University. His research direction includes deep learning and pattern recognition.
<p class="STYLE30"><A href="mailto:qizipeng@buaa.edu.cn">qizipeng@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/luzili.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Zili Liu</P>
<P class="STYLE30">He received the B.S. and M.S. degree from the School of Science, China University of Mining and Technology, Beijing in 2017 and 2021.  He is currently working toward the Phd degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include machine learning, pattern recognition and efficient deep learning.
<p class="STYLE30"><A href="mailto:liuzili@buaa.edu.cn">liuzili@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/ChenKeYan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Keyan Chen</P>
<P class="STYLE30">Keyan Chen received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2019 and 2022. He is currently working toward the PhD degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include remote sensing image processing, multimodal, deep learning and pattern recognition.
<p class="STYLE30"><A href="mailto:kychen@buaa.edu.cn">kychen@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/zhanghaotian.jpeg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Haotian Zhang</P>
<P class="STYLE30">Haotian Zhang received his B.S. degree from the School of Computer and Information Technology, Shanxi University in 2019 and his M.S. degree from the School of Computer Science, Inner Mongolia University in 2022. He is currently working toward the PhD degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include image processing, machine learning and pattern recognition.
<P class="STYLE30"><A href="mailto:haotianzhang@buaa.edu.cn">haotianzhang@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/liuchenyang.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Chenyang Liu</P>
<P class="STYLE30">Chenyang Liu received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2021. He is currently working towards the PhD degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include machine learning and pattern recognition.
<p class="STYLE30"><A href="mailto:liuchenyang@buaa.edu.cn">liuchenyang@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>




<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/chenjianqi.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Jianqi Chen</P>
<P class="STYLE30">Jianqi Chen received his B.S. degree from the Image Processing Center School of Astronautics, Beihang University in 2021. He is currently pursuing his master degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include deep learning, semantic segmentation and object detection.
<p class="STYLE30"><A href="mailto:windvchen@gmail.com">windvchen@gmail.com</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/chenbowen.jpeg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Bowen Chen</P>
<P class="STYLE30">Bowen Chen received the B.S. degree from China University of Petroleum East China, Qingdao, Shandong, China, in 2022. He is doing his mater degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include machine learning and parttern recognition.
<p class="STYLE30"><A href="mailto:chenbowen@buaa.edu.cn">chenbowen@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/dangyi.jpeg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Yi Dang</P>
<P class="STYLE30">Yi Dang received the B.S. degree in the School of Astronautics, Beihang University, Beijing, China, in 2022. She is currently working toward a master degree in the Image Processing Center, School of Astronautics, Beihang University. Her research interests include deep learning and adversarial examples.
<p class="STYLE30"><A href="mailto:18375378@buaa.edu.cn">18375378@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>


<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/zhangyu.jpeg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Yu Zhang</P>
<P class="STYLE30">Yu Zhang received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2022. She is currently working towards the M.S. degree in the Image Processing Center, School of Astronautics, Beihang University. Hers research interests include semantic segmentation, object detection, adversarial example and model robustness.
<p class="STYLE30"><A href="mailto:zhangyu2000@buaa.edu.cn">zhangyu2000@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>


<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/lijunyong.jpeg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Junyong Li</P>
<P class="STYLE30">Junyong Li received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2021. He is currently working towards the M.S. degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include semantic segmentation and cloud detection.
<p class="STYLE30"><A href="mailto:ljy34872@buaa.edu.cn">ljy34872@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>


<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/zhouchenyao.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Chenyao Zhou</P>
<P class="STYLE30">Chenyao Zhou received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2022. He is currently working towards the M.S. degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include pattern recognition and machine learning.
<p class="STYLE30"><A href="mailto:chenyaozhou@buaa.edu.cn">chenyaozhou@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>




<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/yangsongru.jpeg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Songru Yang</P>
<P class="STYLE30">Songru Yang received the B.S. degree in the School of Astronautics, Beihang University, Beijing, China, in 2023. He is currently pursuing his master degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include deep learning and pattern recognition.
<p class="STYLE30"><A href="mailto:19375011@buaa.edu.cn">19375011@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/luguangyu.jpeg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Guangyu Lu</P>
<P class="STYLE30">Guangyu Lu received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2023. He is currently working towards the M.S. degree in the Image Processing Center, School of Astronautics, Beihang University. His research interests include pattern recognition and deep learning.
<p class="STYLE30"><A href="mailto:guangyulu@buaa.edu.cn">guangyulu@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/WangChenDan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Chendan Wang</P>
<P class="STYLE30">Chendan Wang received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2020 and 2023. Her research interests include image generation, machine learning and pattern recognition.
<p class="STYLE30"><A href="mailto:wangchendan@buaa.edu.cn">wangchendan@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/ZhangJing.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Jing Zhang</P>
<P class="STYLE30">Jing Zhang received the B.S. degree from the School of Computer Science and Technology, Xidian University, Xi 'an, Shaanxi, China, in 2020. And she received the M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2023. Her research interests include hyperspectral images, few-shot, Bayesian learning.
<p class="STYLE30"><A href="mailto:zj_cloudia@163.com">zj_cloudia@163.com</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/WuYongChang.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Yongchang Wu</P>
<P class="STYLE30">Yongchang Wu received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2020. He is currently working towards the PhD degree in the School of Astronautics, Beihang University. His research interests include 3-D image processing and pattern recognition.
<p class="STYLE30"><A href="mailto:wuyongchang@buaa.edu.cn">wuyongchang@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>




<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/ZhaoRui.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Rui Zhao</P>
<P class="STYLE30">Rui Zhao received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2019 and 2022. His research interests include machine learning and parttern recognition.
<p class="STYLE30"><A href="mailto:ruizhaoipc@buaa.edu.cn">ruizhaoipc@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/GengXiaoYi.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Xiaoyi Geng</P>
<P class="STYLE30">Xiaoyi Geng received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2019 and 2022. Her research interests include image processing and deep learning.
<p class="STYLE30"><A href="mailto:gxy0809@buaa.edu.cn">gxy0809@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/WangWenJing.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Wenjing Wang</P>
<P class="STYLE30">Wenjing Wang received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2019 and 2022. Her research interests include deep learning and pattern recognition.
<p class="STYLE30"><A href="mailto:346560895@buaa.edu.cn">346560895@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>


<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/WuXi.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Xi Wu</P>
<P class="STYLE30">Xi Wu received his B.S. and PhD degree in School of Astronautics, Beihang University in 2015 and 2022. His research interests include image processing, pattern recognition and machine learning. 
<P class="STYLE30"><A href="mailto:xiwu100@126.com">xiwu100@126.com</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="66">
<TBODY>
<TR>
<TD width="188"><IMG src="imgs/students/linghaoling.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Haoning Lin </P>
<P class="STYLE30">Haoning Lin received the B.S. and PhD degree from the School of Astronautics, Beihang University, Beijing, China, in 2013 and 2021. His research interests include machine learning and parttern recognition.</P>
<P class="STYLE30"><A href="mailto:linhn1911@gmail.com">linhn1911@gmail.com</A></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/LeiSen.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Sen Lei</P>
<P class="STYLE30">Sen Lei received the B.S. and PhD degree from the School of Astronautics, Beihang University, Beijing, China, in 2015 and 2021. His research interests include image processing, pattern recognition and machine learning. 
<P class="STYLE30"><A href="mailto:leisen0604@163.com">senlei@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/ztk.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Tiankun Zhang</P>
<P class="STYLE30">Tiankun Zhang received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2018 and 2021. His research interests include deep learning and pattern recognition.
<P class="STYLE30"><A href="mailto:zhangtiankun@buaa. edu.cn">zhangtiankun@buaa. edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/haokun.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Kun Hao</P>
<P class="STYLE30">Kun Hao received the B.S. and M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2018 and 2021. Her research interests include image processing and deep learning.
<p class="STYLE30"><A href="mailto:haokun@buaa.edu.cn">haokun@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/MaXiaofeng.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Xiaofeng Ma</P>
<P class="STYLE30">Xiaofeng Ma received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2017. He received his M.S. degree in 2019 from Beihang University. His research interests include machine learning and pattern recognition.
<P class="STYLE30"><A href="mailto:max15@buaa.edu.cn">max15@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>


<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/zhoumin.png" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Min Zhou</P>
<P class="STYLE30">Min Zhou received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2016. She received her M.S. degree in 2018 from Beihang University.Her research interests include deep learning and pattern recognition.
<P class="STYLE30"><A href="mailto:minzhou_eureka@buaa.edu.cn">minzhou_eureka@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/shitianyang.png" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Tianyang Shi</P>
<P class="STYLE30">Tianyang Shi received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2016. He received his M.S. degree in 2018 from Beihang University. His research interests include image processing, pattern recognition and deep learning.
<P class="STYLE30"><A href="mailto:shitianyang@buaa.edu.cn">shitianyang@buaa.edu.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="223">
<TBODY>
<TR>
<TD height="256" width="188"><IMG src="imgs/students/xuxia.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Xia Xu</P>
<P class="STYLE30">Xia Xu received the M.S. degree and the B.S. degree from Yanshan University, Qinhuangdao, China, in 2015 and 2012 respectively. She received her PhD degree in 2019 from Beihang University. She is now working in the College of Computer Science, Nankai University . Her research interests include hyperspectral image sparse unmixing and pattern recognition.</P><SPAN class="STYLE30"><A href="mailto:xuxiajnz@163.com">xuxiajnz@163.com</A></SPAN></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="223">
<TBODY>
<TR>
<TD height="256" width="188"><IMG src="imgs/students/PanBin.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Bin Pan</P>
<P class="STYLE30">Bin Pan received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2013. He received his PhD degree in 2019 from Beihang University. He is now working in the School of Statistics and Data Science, Nankai University. His research interests include hyperspectral image processing and pattern recognition.</P><SPAN class="STYLE30"><A href="mailto:panbin@buaa.edu.cn">panbin@buaa.edu.cn</A></SPAN></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="223">
<TBODY>
<TR>
<TD height="256" width="188"><IMG src="imgs/students/zouzhengxia.JPG" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Zhengxia Zou</P>
<P class="STYLE30">Zhengxia Zou received his B.S. degree and his Ph.d degree from the School of Astronautics, Beihang University in 2013 and 2018, respectively. He is now working in the University of Michigan as postdoc research fellow. His research interests include machine learning, image processing and computer vision.
</P><SPAN class="STYLE30"><A href="mailto:zhengxiazou@gmail.com">zhengxiazou@gmail.com</A></SPAN></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="66">
<TBODY>
<TR>
<TD width="188"><SPAN class="STYLE20"><IMG alt="" src="imgs/students/yangshuo.jpg" width="150" height="200"> </SPAN></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Shuo Yang</P>
<P class="STYLE30">Shuo Yang received the B.S. degree from Shandong University, Weihai, China, in 2009 and&nbsp;the Ph.d. degree in the Image Processing Center, School of Astronautics, Beihang University in 2016. He is currently working in the China Astronautics Tech Company.&nbsp;<BR>His research interests include hyperspectral image processing, and pattern recognition.</P><SPAN class="STYLE30"><A href="mailto:yangshuodf@126.com">yangshuodf@126.com</A></SPAN></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="66">
<TBODY>
<TR>
<TD width="188"><SPAN class="STYLE20"><IMG alt="" src="imgs/students/anzhenyu.jpg" width="150" height="200"> </SPAN></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Zhenyu An</P>
<P class="STYLE30">Zhenyu An received the B.S. degree and the Ph.d degree from the School of Astronautics, Beihang University, Beijing, China, in 2010 and 2016,respectively. He is currently working in the 28th Research Institute of China Electronics Technology Group Corporation.His research interests include hyperspectral image processing and pattern recognition.</P><SPAN class="STYLE30"><A href="mailto:an.zhenyu.buaa@gmail.com">an.zhenyu.buaa@gmail.com</A></SPAN></TD></TR></TBODY></TABLE>
<HR>


<TABLE border="0" width="533" height="243">
<TBODY>
<TR>
<TD height="275" width="188"><IMG src="imgs/students/TanXueyan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Xueyan Tan</P>
<P class="STYLE30">XueYan Tan received the B.S. degree from the School of Yanshan University, Qinhuangdao, China, in 2007 and the M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2011. During the graduate study period, her main research interests is hyperspectral image unmixing. She is currently works at Beijing Science &amp; Technology Consulting Center. </P>
<P class="STYLE30"><SPAN class="STYLE32"><A href="mailto:Txueyan163@163.com">Txueyan163@163.com</A></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="243">
<TBODY>
<TR>
<TD height="275" width="188"><IMG src="imgs/students/ZhaiXinya.jpg" width="150"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Xinya Zhai</P>
<P class="STYLE30">Xinya Zhai received the B.S. degree from ShanDong University, China, in 2009 and the M.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2012. She worked in Dayang Technology Development Inc. for nearly two years. She is currently working in Beijing huaruan Hengxin Technology Technology Development Co. Ltd. in the field of electric power. </P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="258">
<TBODY>
<TR>
<TD height="311" width="188"><IMG src="imgs/students/JunWu.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Jun Wu</P>
<P class="STYLE30" align="left">Jun Wu received the B.S. degree from the School of Computer Science, Wuhan University of Science and Engineering, Wuhan, China, in 2009 and the M.S degree from the School of Astronautics, Beihang University, Beijing, China, in 2012. He is currently working at Space star technology co., LTD.</P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="201">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/zhufeiyun.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Feiyun Zhu</P>
<P class="STYLE30">Feiyun Zhu received his B.S. degree in Image Processing Center of Beihang University, Beijing, China, in 2010. He is currently pursuing his Ph.D. degree in Institute of Automation, Chinese Academy of Sciences.</P>
<P class="STYLE30"><A href="mailto:fyzhu@nlpr.ia.ac.cn">fyzhu@nlpr.ia.ac.cn</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="258">
<TBODY>
<TR>
<TD height="311" width="188"><IMG src="imgs/students/qinzhen.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Zhen Qin</P>
<P class="STYLE30" align="left">Zhen Qin received the B.S. and M.S. degrees from the School of Astronautics, Beihang University, Beijing, China, in 2010 and 2013, respectively. She is currently doing research on developing crypto IP kernels of SoC in Xi'an Microelectronics Technology Institute, CASA. During the graduate study period, her research interests included hyperspectral image processing and pattern recognition.</P>
<P class="STYLE30"><A href="mailto:jane19871212@126.com">jane19871212@126.com</A></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="313" width="188"><IMG src="imgs/students/longjiao.JPG" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Jiao Long</P>
<P class="STYLE30">Jiao Long recieved the B.S. degree from the Department of Automation Engineering, Northeast University at Qinhuangdao, Qinhuangdao, China, in 2011 and the M.S degree from the School of Astronautics, Beihang University, Beijing, China, in 2014. <BR>Her research interests include image dehazing and object detection.</P>
<P class="STYLE30"><SPAN class="STYLE32"><A href="mailto:longjiao1208@gmail.com">longjiao1208@gmail.com</A></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="243">
<TBODY>
<TR>
<TD height="275" width="188"><IMG src="imgs/students/liuliu.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Liu Liu</P>
<P class="STYLE30">Liu Liu received the B.S. degree from the School of Science, Hebei University of Technology, Tianjin, China, in 2011 and the M.S degree from the School of Astronautics, Beihang University, Beijing, China, in 2014. She is currently working toward the Ph.D. degree in university of technology sydney (UTS). Her research interests include pattern recognition, machine learning, sparse coding and target detection.</P>
<P class="STYLE30"><SPAN class="STYLE32"><A href="mailto:liuliubh@gmail.com">liuliubh@gmail.com</A></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="201">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/durenzhana.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Zhana Duren</SPAN></P>
<P class="STYLE30">Zhana Duren received the bachelor degree from the School of Mathematics and Systems Science, Beihang university, Beijing, China, in 2012. He has been at Zhenwei Shi's Laboratory since 2010.9 to 2012.6. During this period he did some research about hyperspectral imagery as his undergraduate graduation design. He is currently a master degree candidate student in academy of mathematics and systems science (AMSS), Chinese academy of science (CAS), Beijing, China, since 2012. His main research interests include bioinformatics, system biology and hyperspectral imagery.</P>
<P><SPAN class="STYLE30"><A href="mailto:durenzn@amss.ac.cn">durenzn@amss.ac.cn</A></SPAN></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="66">
<TBODY>
<TR>
<TD width="188"><IMG src="imgs/students/tangwei.png" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Wei Tang</P>
<P class="STYLE30">Wei Tang received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2012 and the M.S degree from the School of Astronautics, Beihang University, Beijing, China, in 2015.He is currently working toward the Ph.D degree in Northwestern University(NWU) in US.His research interests include sparse representation, hyperspectral image processing, and pattern recognition.</P>
<P class="STYLE30"><SPAN class="STYLE32"><A href="mailto:tangwei@sa.buaa.edu.cn">tangwei@sa.buaa.edu.cn</A></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="215">
<TBODY>
<TR>
<TD width="188"><IMG src="imgs/students/chenquan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Quan Chen</P>
<P class="STYLE30">Quan Chen received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2012 and the M.S degree from the School of Astronautics, Beihang University, Beijing, China, in 2015. He is currently working in Alibaba Group. His research interests include remote sensing technologies such as hyperspectral image fusion, computer vision tasks such as image retrieval, and object detection.</P>
<P class="STYLE30"><SPAN class="STYLE32"><A href="mailto:chenquan.buaa@gmail.com">chenquan.buaa@gmail.com</A></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="66">
<TBODY>
<TR>
<TD width="188"><IMG src="imgs/students/yuxinran.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Xinran Yu</P>
<P class="STYLE30">Xinran Yu received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2012 and the M.S degree from the School of Astronautics, Beihang University, Beijing, China, in 2015. He is currently working in the 28th Research Institute of China Electronics Technology Group Corporation. His research interests include optical image processing, optical target detection and classification and pattern recognition.<BR><BR><A href="mailto:yuxinran.buaa@gmail.com">yuxinran.buaa@gmail.com</A></P></TD></TR></TBODY></TABLE>
<HR>


<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/zhanglu.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Lu Zhang</P>
<P class="STYLE30">Lu Zhang received the B.S. degree from the University of Science and Technology Beijing, Beijing, China, in 2013，and received the M.S. degree in the Image Processing Center, School of Astronautics, Beihang University in 2016.<BR>His research interests include deep learning ,neural network and pattern recognition.</P>
<P class="STYLE30"><A href="mailto:jiangaihua312@gmail.com">jiangaihua312@gmail.com</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/wangdan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Dan Wang</P>
<P class="STYLE30">Dan Wang received the B.S. degree from the School of Astronautics, Beihang University, Beijing, China, in 2014. She is currently working toward her M.S. degree in the Image Processing Center, School of Astronautics, Beihang University. Her research interests include machine learning, pattern recognition.</P>
<P class="STYLE30"><A href="mailto:jiangaihua312@gmail.com">wangdan16@hotmail.com</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>

<TABLE border="0" width="533" height="239">
<TBODY>
<TR>
<TD height="273" width="188"><IMG src="imgs/students/luoqinhan.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Qinhan Luo</P>
<P class="STYLE30">Qinhan Luo received the B.S. degree from the School of Automation Science and Electrical Engineering, Beihang University, Beijing, China, in 2013.He is currently working toward the M.S. degree in the Image Processing Center, School of Astronautics, Beihang University.<BR>His research interests include deep learning, neural network and pattern recognition.</P>
<P class="STYLE30"><A href="mailto:jiangaihua312@gmail.com">sherlock_homels@163.com</A></P>
<P class="STYLE21"></SPAN></P></TD></TR></TBODY></TABLE>
<HR>



<TABLE border="0" width="533" height="258">
<TBODY>
<TR>
<TD height="311" width="188"><IMG src="imgs/students/zhongweihuang.jpg" width="150" height="200"></TD>
<TD width="329">
<P class="STYLE22 STYLE15 STYLE31">Zhongwei Huang</P>
<P class="STYLE30" align="left">Zhongwei Huang received the bachelor degree from the School of Mathematics and Systems Science, Beihang university, Beijing, China, in 2013. He has been at Zhenwei Shi's Laboratory since 2011.12 to 2013.6. During this period he did some research about hyperspectral imagery as his undergraduate graduation design. He is currently a master degree candidate student in University of New Brunswick, Canada, since 2013. His main research interests include remote sensing and machine learning.</P>
<P class="STYLE30"><A href="mailto:zhongwei.huang@unb.ca">zhongwei.huang@unb.ca</A></P></TD></TR></TBODY></TABLE>
<HR>
'''


template = '''---
name: Keyan Chen
startdate: [2015-01-01]
enddate: [2019-09-01]
image: /static/img/members/none.jpg # 365 x 365 pixels, 72 dpi
\# altimage: /static/img/members/chen_pb.jpg #365 x 365 pixels, 72 dpi
position: "M.S. Student"
timeline_positions: ["M.S. Student (2019-2022)"]
\# subsequent:  update once you become an alumnus
pronouns: he/him/his # personal pronouns
email: kychen@buaa.edu.cn # Preferred public email address
scholar: 
website: 
beihang:
twitter:
linkedin:
github: 
researchgate:
dblp: 
orcid: 
description: "Keyan Chen"
---'''

import pandas as pd
import re
import os
from bs4 import BeautifulSoup
import requests

# data = BeautifulSoup(t)
# t = data.text
# t = t.split('\n')
# t = [i for i in t if i != '' and len(i) > 2]
# os.makedirs('content/authors', exist_ok=True)
# idx = 0
# while idx < len(t):
#     tmp_template = copy.deepcopy(template)
#     name = t[idx].strip()
#     if len(name) > 20:
#         print(name)
#     idx += 1
#     description = ''
#     while '@' not in t[idx].strip():
#         description += t[idx] + '\n'
#         idx += 1
#
#     email = t[idx].strip()
#     idx += 1
#     assert '@' in email
#     tmp_template = tmp_template.replace('name: Keyan Chen', 'name: ' + name)
#     tmp_template = tmp_template.replace('description: "Keyan Chen"', 'description: "' + description + '"')
#     tmp_template = tmp_template.replace('email: kychen@buaa.edu.cn', 'email: ' + email)
#     name = name.replace(' ', '_').lower()
#     with open('content/authors/' + name + '.md', 'w') as f:
#         f.write(tmp_template)

pattern = re.compile(r"STYLE22 STYLE15 STYLE31")
matches = pattern.finditer(t)
m = []
for match in matches:
    m.append(t[match.end()+2:match.end()+19])
m = [i for i in m if i != '' and len(i) > 2]
print(len(m))
m = [x.split('/P')[0][:-1] for x in m]
m.sort()

for i in m:
    os.makedirs(f'to_finish/{i}', exist_ok=True)
print(len(m))
print(m)
pass


