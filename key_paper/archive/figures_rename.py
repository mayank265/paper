
algos = ['RF', 'REPT', 'RT']
algos =['dt', 'XGB', 'et','MLP']
graph_types = ['line_chart', 'bar_chart', 'line_scatter', 'box_plot', "scatter_chart", "spider_chart", "taylor_chart","algorithm_explanation","radar_chart"]
empirical_or_existing_authors = ['abghani', 'vanvel', 'hutoff',"nalluri"]
main_figures = ['architecture', 'correlation_heatmap']
error_metric=["agreement_index", "bias", "cc", "covariance", "decomposed_mse", "kge", "log_p", "log_nashsutcliffe", "mae", "mse", "nse", "pbias", "rmse", "relative_rmse", "r2", "rsr", "volume_error"]
key="froude1"

# concat_func = lambda x,y: x + "" + str(y)


for x in algos:
    for y in graph_types:
        print("p_",x.lower(),"_",y.lower(),"_",key,sep='')

for x in empirical_or_existing_authors:
    for y in graph_types:
        print("e_",x.lower(),"_",y.lower(),"_",key,sep='')

for x in main_figures:
    print(x.lower(),"_",key,sep='')

for x in error_metric:
    for y in graph_types:
        # print(x.lower(), "_", y.lower(), "_", key, sep='')
        print("overall_", x.lower(),"_",y.lower(),"_",key,sep='')

print("overall_box_plot_all_algos_",key,sep='')
print("overall_scatter_all_algos_",key,sep='')