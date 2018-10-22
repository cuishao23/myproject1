from django.shortcuts import render
from django.views.generic import View
from goods.models import *

# class IndexView(View):
#     def get(self,request):
#         # 获取商品的种类信息
#         goodstype_list = GoodsType.objects.all()
#         # 准备数据字典
#         context = {'goodstype_list':goodstype_list}
#         #返回首页
#         return render(request,'test_index.html',context)


class IndexView(View):
    def get(self,request):
        '''显示首页'''
        # 获取商品的种类信息
        types = GoodsType.objects.all()
        #获取首页轮播商品信息
        goods_banners=IndexGoodsBanner.objects.all().order_by('index')
        #获取首页促销活动信息
        promotion_banners=IndePromotionBanner.objects.all().order_by('index')

        #获取首页分类商品展示信息
        for type in types: #GoodsType
            #获取type种类首页分类的商品的图片展示信息
            image_banners=IndexTypeGoodsBanner.objects.filter(type=type,display_type=1).order_by('index')
            #获取type种类首页分类的商品的文字展示信息
            title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

            #动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
            type.image_banners=image_banners
            type.title_banners = title_banners
        #获取用户购物车中商品的数目，暂时设置为0，待完善
        cart_count=0

        #组织模板上下文
        context={
            'types':types,
            'goods_banners':goods_banners,
            'promotion_banners':promotion_banners,
            'cart_count':cart_count,
        }
        #使用模板
        return render(request,'index.html',context)


class DetailView(View):
    print('DetailView')
    def get(self,request):
        return render(request, 'detail.html')








