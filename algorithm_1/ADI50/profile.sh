sudo nvprof -f -o algorithm_1.timeline ../bin/total_force_cuda.x config.txt
sudo nvprof -f --analysis-metrics -o algorithm_2.metrics ../bin/total_force_cuda.x config.txt
