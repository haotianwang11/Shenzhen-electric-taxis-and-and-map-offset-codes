import math
from scipy import stats
def e_step(pi, p, q, sample):
	# 求导过程代码实现
    A=((len(sample)*p*(1-q)+ sum([pi for i in range(len(sample))]))/p-len(sample))
    B=(sum([pi for i in range(len(sample))])/q-((len(sample)*p*(1-q))/(1-q)))
    return A

def m_step(u,x,q,sample):
	# 更新参数
    A = ((len(sample) * p * (1 - q) + sum([pi for i in range(len(sample))])) / len(sample))
    B = sum([pi for i in range(len(sample))])/((len(sample) * p * (1 - q) + sum([pi for i in range(len(sample))])))
    return [A,B]

def run(sample, pi, p, q, iter_num):
    print(sample)
    for i in range(iter_num):
        u=e_step(pi, p, q, sample)
        # 停止条件
        if [p,q]==m_step(pi, p, q, sample):
            break
        else:
            [p,q]=m_step(pi, p, q, sample)
    print(p*q)
if __name__ =="__main__":
    # 观察数据
    sample = stats.poisson.rvs(mu=50, size=100, random_state=3)
    [pi, p, q] = [0.62, 0.4, 0.7]
    run(sample,pi,p,q,100)
