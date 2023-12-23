# Module 1: AI Introduction

# Module 2: Eyes Blink Engine

# Module 3: Mouse and Keyboard tracker

# Module 4 - Activity and Inactivity Engine

# Module 5 - Build Eyes tracker

# Module 6 - APP desktop

# asus

""" Text Mining
(joyrl) qaz1214@QiyudeMacBook-Pro joyrl-main % joyrl --yaml ./presets/ClassControl/CartPole-v1/CartPole-v1_DQN.yaml
2023-12-22 10:17:51 - Log - INFO: - General Configs:
2023-12-22 10:17:51 - Log - INFO: - ================================================================================
2023-12-22 10:17:51 - Log - INFO: -         Name        	       Value        	        Type        
2023-12-22 10:17:51 - Log - INFO: -       env_name      	        gym         	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -      algo_name      	        DQN         	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -         mode        	       train        	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -     worker_mode     	       dummy        	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -     learner_mode    	       serial       	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -        device       	        cpu         	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -         seed        	         1          	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -     max_episode     	        100         	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -       max_step      	        200         	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -     collect_traj    	         0          	   <class 'bool'>   
2023-12-22 10:17:51 - Log - INFO: -    n_interactors    	         1          	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -      n_learners     	         1          	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -     share_buffer    	         1          	   <class 'bool'>   
2023-12-22 10:17:51 - Log - INFO: -     online_eval     	         1          	   <class 'bool'>   
2023-12-22 10:17:51 - Log - INFO: - online_eval_episode 	         10         	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -    model_save_fre   	        500         	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -   load_checkpoint   	         0          	   <class 'bool'>   
2023-12-22 10:17:51 - Log - INFO: -      load_path      	Train_single_CartPole-v1_DQN_20230515-211721	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -   load_model_step   	        best        	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: - interact_summary_fre	         1          	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -  policy_summary_fre 	        100         	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: - ================================================================================
2023-12-22 10:17:51 - Log - INFO: - Algo Configs:
2023-12-22 10:17:51 - Log - INFO: - ================================================================================
2023-12-22 10:17:51 - Log - INFO: -         Name        	       Value        	        Type        
2023-12-22 10:17:51 - Log - INFO: -    epsilon_start    	        0.95        	  <class 'float'>   
2023-12-22 10:17:51 - Log - INFO: -     epsilon_end     	        0.01        	  <class 'float'>   
2023-12-22 10:17:51 - Log - INFO: -    epsilon_decay    	        500         	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -        gamma        	        0.95        	  <class 'float'>   
2023-12-22 10:17:51 - Log - INFO: -          lr         	       0.0001       	  <class 'float'>   
2023-12-22 10:17:51 - Log - INFO: -     buffer_type     	     REPLAY_QUE     	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -     buffer_size     	       100000       	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -      batch_size     	        128         	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -    target_update    	         4          	   <class 'int'>    
2023-12-22 10:17:51 - Log - INFO: -     value_layers    	[{'layer_type': 'linear', 'layer_size': [256], 'activation': 'relu'}, {'layer_type': 'linear', 'layer_size': [256], 'activation': 'relu'}]	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: - ================================================================================
2023-12-22 10:17:51 - Log - INFO: - Env Configs:
2023-12-22 10:17:51 - Log - INFO: - ================================================================================
2023-12-22 10:17:51 - Log - INFO: -         Name        	       Value        	        Type        
2023-12-22 10:17:51 - Log - INFO: -          id         	    CartPole-v1     	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -     render_mode     	        None        	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -       wrapper       	        None        	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: -    ignore_params    	['wrapper', 'ignore_params']	   <class 'str'>    
2023-12-22 10:17:51 - Log - INFO: - ================================================================================
2023-12-22 10:17:51 - Log - INFO: - [OnlineTester] Start online tester!
2023-12-22 10:17:51 - Log - INFO: - [ModelMgr.init] Start model manager!
2023-12-22 10:17:51 - Log - INFO: - [Recorder.run] Start recorder!
2023-12-22 10:17:51 - Log - INFO: - [Collector.init] Start collector!
2023-12-22 10:17:51 - Log - INFO: - [Trainer.run] Start training!
2023-12-22 10:17:52 - Log - INFO: - Interactor 0 finished episode 0 with reward 16.000 in 16 steps
2023-12-22 10:17:53 - Log - INFO: - Interactor 0 finished episode 1 with reward 18.000 in 18 steps
2023-12-22 10:17:54 - Log - INFO: - Interactor 0 finished episode 2 with reward 34.000 in 34 steps
2023-12-22 10:17:54 - Log - INFO: - Interactor 0 finished episode 3 with reward 13.000 in 13 steps
2023-12-22 10:17:55 - Log - INFO: - Interactor 0 finished episode 4 with reward 18.000 in 18 steps
2023-12-22 10:17:56 - Log - INFO: - Interactor 0 finished episode 5 with reward 19.000 in 19 steps
2023-12-22 10:17:57 - Log - INFO: - Interactor 0 finished episode 6 with reward 15.000 in 15 steps
2023-12-22 10:17:57 - Log - INFO: - Interactor 0 finished episode 7 with reward 22.000 in 22 steps
2023-12-22 10:17:57 - Log - INFO: - test_step: 0, online_eval_reward: 9.600
2023-12-22 10:17:57 - Log - INFO: - current test step obtain a better online_eval_reward: 9.600, save the best model!
2023-12-22 10:17:58 - Log - INFO: - Interactor 0 finished episode 8 with reward 36.000 in 36 steps
2023-12-22 10:17:58 - Log - INFO: - Interactor 0 finished episode 9 with reward 17.000 in 17 steps
2023-12-22 10:17:59 - Log - INFO: - Interactor 0 finished episode 10 with reward 13.000 in 13 steps
2023-12-22 10:18:00 - Log - INFO: - Interactor 0 finished episode 11 with reward 32.000 in 32 steps
2023-12-22 10:18:00 - Log - INFO: - Interactor 0 finished episode 12 with reward 19.000 in 19 steps
2023-12-22 10:18:01 - Log - INFO: - Interactor 0 finished episode 13 with reward 15.000 in 15 steps
2023-12-22 10:18:01 - Log - INFO: - Interactor 0 finished episode 14 with reward 12.000 in 12 steps
2023-12-22 10:18:01 - Log - INFO: - Interactor 0 finished episode 15 with reward 18.000 in 18 steps
2023-12-22 10:18:02 - Log - INFO: - Interactor 0 finished episode 16 with reward 10.000 in 10 steps
2023-12-22 10:18:02 - Log - INFO: - Interactor 0 finished episode 17 with reward 11.000 in 11 steps
2023-12-22 10:18:02 - Log - INFO: - Interactor 0 finished episode 18 with reward 13.000 in 13 steps
2023-12-22 10:18:03 - Log - INFO: - Interactor 0 finished episode 19 with reward 15.000 in 15 steps
2023-12-22 10:18:03 - Log - INFO: - Interactor 0 finished episode 20 with reward 10.000 in 10 steps
2023-12-22 10:18:03 - Log - INFO: - Interactor 0 finished episode 21 with reward 13.000 in 13 steps
2023-12-22 10:18:04 - Log - INFO: - Interactor 0 finished episode 22 with reward 11.000 in 11 steps
2023-12-22 10:18:04 - Log - INFO: - Interactor 0 finished episode 23 with reward 10.000 in 10 steps
2023-12-22 10:18:04 - Log - INFO: - Interactor 0 finished episode 24 with reward 13.000 in 13 steps
2023-12-22 10:18:05 - Log - INFO: - Interactor 0 finished episode 25 with reward 18.000 in 18 steps
2023-12-22 10:18:05 - Log - INFO: - Interactor 0 finished episode 26 with reward 14.000 in 14 steps
2023-12-22 10:18:05 - Log - INFO: - Interactor 0 finished episode 27 with reward 10.000 in 10 steps
2023-12-22 10:18:06 - Log - INFO: - Interactor 0 finished episode 28 with reward 11.000 in 11 steps
2023-12-22 10:18:06 - Log - INFO: - Interactor 0 finished episode 29 with reward 10.000 in 10 steps
2023-12-22 10:18:07 - Log - INFO: - Interactor 0 finished episode 30 with reward 17.000 in 17 steps
2023-12-22 10:18:07 - Log - INFO: - Interactor 0 finished episode 31 with reward 12.000 in 12 steps
2023-12-22 10:18:07 - Log - INFO: - Interactor 0 finished episode 32 with reward 14.000 in 14 steps
2023-12-22 10:18:08 - Log - INFO: - Interactor 0 finished episode 33 with reward 9.000 in 9 steps
2023-12-22 10:18:08 - Log - INFO: - Interactor 0 finished episode 34 with reward 10.000 in 10 steps
2023-12-22 10:18:08 - Log - INFO: - Interactor 0 finished episode 35 with reward 12.000 in 12 steps
2023-12-22 10:18:09 - Log - INFO: - Interactor 0 finished episode 36 with reward 14.000 in 14 steps
2023-12-22 10:18:09 - Log - INFO: - Interactor 0 finished episode 37 with reward 9.000 in 9 steps
2023-12-22 10:18:09 - Log - INFO: - Interactor 0 finished episode 38 with reward 10.000 in 10 steps
2023-12-22 10:18:09 - Log - INFO: - Interactor 0 finished episode 39 with reward 13.000 in 13 steps
2023-12-22 10:18:10 - Log - INFO: - Interactor 0 finished episode 40 with reward 10.000 in 10 steps
2023-12-22 10:18:10 - Log - INFO: - Interactor 0 finished episode 41 with reward 9.000 in 9 steps
2023-12-22 10:18:10 - Log - INFO: - Interactor 0 finished episode 42 with reward 9.000 in 9 steps
2023-12-22 10:18:11 - Log - INFO: - Interactor 0 finished episode 43 with reward 11.000 in 11 steps
2023-12-22 10:18:11 - Log - INFO: - test_step: 500, online_eval_reward: 9.500
2023-12-22 10:18:11 - Log - INFO: - Interactor 0 finished episode 44 with reward 12.000 in 12 steps
2023-12-22 10:18:12 - Log - INFO: - Interactor 0 finished episode 45 with reward 31.000 in 31 steps
2023-12-22 10:18:13 - Log - INFO: - Interactor 0 finished episode 46 with reward 40.000 in 40 steps
2023-12-22 10:18:16 - Log - INFO: - Interactor 0 finished episode 47 with reward 85.000 in 85 steps
2023-12-22 10:18:17 - Log - INFO: - Interactor 0 finished episode 48 with reward 51.000 in 51 steps
2023-12-22 10:18:19 - Log - INFO: - Interactor 0 finished episode 49 with reward 72.000 in 72 steps
2023-12-22 10:18:21 - Log - INFO: - Interactor 0 finished episode 50 with reward 57.000 in 57 steps
2023-12-22 10:18:23 - Log - INFO: - Interactor 0 finished episode 51 with reward 65.000 in 65 steps
2023-12-22 10:18:26 - Log - INFO: - Interactor 0 finished episode 52 with reward 104.000 in 104 steps
2023-12-22 10:18:26 - Log - INFO: - test_step: 1000, online_eval_reward: 49.600
2023-12-22 10:18:26 - Log - INFO: - current test step obtain a better online_eval_reward: 49.600, save the best model!
2023-12-22 10:18:29 - Log - INFO: - Interactor 0 finished episode 53 with reward 105.000 in 105 steps
2023-12-22 10:18:31 - Log - INFO: - Interactor 0 finished episode 54 with reward 62.000 in 62 steps
2023-12-22 10:18:33 - Log - INFO: - Interactor 0 finished episode 55 with reward 64.000 in 64 steps
2023-12-22 10:18:35 - Log - INFO: - Interactor 0 finished episode 56 with reward 66.000 in 66 steps
2023-12-22 10:18:37 - Log - INFO: - Interactor 0 finished episode 57 with reward 58.000 in 58 steps
2023-12-22 10:18:39 - Log - INFO: - Interactor 0 finished episode 58 with reward 64.000 in 64 steps
2023-12-22 10:18:41 - Log - INFO: - Interactor 0 finished episode 59 with reward 70.000 in 70 steps
2023-12-22 10:18:41 - Log - INFO: - test_step: 1500, online_eval_reward: 66.400
2023-12-22 10:18:41 - Log - INFO: - current test step obtain a better online_eval_reward: 66.400, save the best model!
2023-12-22 10:18:42 - Log - INFO: - Interactor 0 finished episode 60 with reward 66.000 in 66 steps
2023-12-22 10:18:44 - Log - INFO: - Interactor 0 finished episode 61 with reward 60.000 in 60 steps
2023-12-22 10:18:46 - Log - INFO: - Interactor 0 finished episode 62 with reward 81.000 in 81 steps
2023-12-22 10:18:48 - Log - INFO: - Interactor 0 finished episode 63 with reward 68.000 in 68 steps
2023-12-22 10:18:50 - Log - INFO: - Interactor 0 finished episode 64 with reward 73.000 in 73 steps
2023-12-22 10:18:52 - Log - INFO: - Interactor 0 finished episode 65 with reward 66.000 in 66 steps
2023-12-22 10:18:54 - Log - INFO: - Interactor 0 finished episode 66 with reward 74.000 in 74 steps
2023-12-22 10:18:55 - Log - INFO: - test_step: 2000, online_eval_reward: 72.900
2023-12-22 10:18:55 - Log - INFO: - current test step obtain a better online_eval_reward: 72.900, save the best model!
2023-12-22 10:18:56 - Log - INFO: - Interactor 0 finished episode 67 with reward 72.000 in 72 steps
2023-12-22 10:18:59 - Log - INFO: - Interactor 0 finished episode 68 with reward 85.000 in 85 steps
2023-12-22 10:19:02 - Log - INFO: - Interactor 0 finished episode 69 with reward 100.000 in 100 steps
2023-12-22 10:19:05 - Log - INFO: - Interactor 0 finished episode 70 with reward 111.000 in 111 steps
2023-12-22 10:19:09 - Log - INFO: - Interactor 0 finished episode 71 with reward 122.000 in 122 steps
2023-12-22 10:19:11 - Log - INFO: - test_step: 2500, online_eval_reward: 128.800
2023-12-22 10:19:11 - Log - INFO: - current test step obtain a better online_eval_reward: 128.800, save the best model!
2023-12-22 10:19:13 - Log - INFO: - Interactor 0 finished episode 72 with reward 134.000 in 134 steps
2023-12-22 10:19:19 - Log - INFO: - Interactor 0 finished episode 73 with reward 193.000 in 193 steps
2023-12-22 10:19:25 - Log - INFO: - Interactor 0 finished episode 74 with reward 200.000 in 200 steps
2023-12-22 10:19:26 - Log - INFO: - test_step: 3000, online_eval_reward: 198.600
2023-12-22 10:19:26 - Log - INFO: - current test step obtain a better online_eval_reward: 198.600, save the best model!
2023-12-22 10:19:30 - Log - INFO: - Interactor 0 finished episode 75 with reward 200.000 in 200 steps
2023-12-22 10:19:36 - Log - INFO: - Interactor 0 finished episode 76 with reward 200.000 in 200 steps
2023-12-22 10:19:41 - Log - INFO: - test_step: 3500, online_eval_reward: 200.000
2023-12-22 10:19:41 - Log - INFO: - current test step obtain a better online_eval_reward: 200.000, save the best model!
2023-12-22 10:19:42 - Log - INFO: - Interactor 0 finished episode 77 with reward 200.000 in 200 steps
2023-12-22 10:19:48 - Log - INFO: - Interactor 0 finished episode 78 with reward 200.000 in 200 steps
2023-12-22 10:19:55 - Log - INFO: - Interactor 0 finished episode 79 with reward 200.000 in 200 steps
2023-12-22 10:19:56 - Log - INFO: - test_step: 4000, online_eval_reward: 196.000
2023-12-22 10:20:01 - Log - INFO: - Interactor 0 finished episode 80 with reward 200.000 in 200 steps
2023-12-22 10:20:08 - Log - INFO: - Interactor 0 finished episode 81 with reward 200.000 in 200 steps
2023-12-22 10:20:13 - Log - INFO: - test_step: 4500, online_eval_reward: 200.000
2023-12-22 10:20:13 - Log - INFO: - current test step obtain a better online_eval_reward: 200.000, save the best model!
2023-12-22 10:20:14 - Log - INFO: - Interactor 0 finished episode 82 with reward 200.000 in 200 steps
2023-12-22 10:20:21 - Log - INFO: - Interactor 0 finished episode 83 with reward 200.000 in 200 steps
2023-12-22 10:20:27 - Log - INFO: - Interactor 0 finished episode 84 with reward 200.000 in 200 steps
2023-12-22 10:20:28 - Log - INFO: - test_step: 5000, online_eval_reward: 191.000
2023-12-22 10:20:33 - Log - INFO: - Interactor 0 finished episode 85 with reward 200.000 in 200 steps
2023-12-22 10:20:39 - Log - INFO: - Interactor 0 finished episode 86 with reward 200.000 in 200 steps
2023-12-22 10:20:44 - Log - INFO: - test_step: 5500, online_eval_reward: 182.000
2023-12-22 10:20:45 - Log - INFO: - Interactor 0 finished episode 87 with reward 200.000 in 200 steps
2023-12-22 10:20:52 - Log - INFO: - Interactor 0 finished episode 88 with reward 200.000 in 200 steps
2023-12-22 10:20:59 - Log - INFO: - Interactor 0 finished episode 89 with reward 200.000 in 200 steps
2023-12-22 10:21:01 - Log - INFO: - test_step: 6000, online_eval_reward: 196.900
2023-12-22 10:21:05 - Log - INFO: - Interactor 0 finished episode 90 with reward 200.000 in 200 steps
2023-12-22 10:21:12 - Log - INFO: - Interactor 0 finished episode 91 with reward 200.000 in 200 steps
2023-12-22 10:21:16 - Log - INFO: - test_step: 6500, online_eval_reward: 189.600
2023-12-22 10:21:17 - Log - INFO: - Interactor 0 finished episode 92 with reward 197.000 in 197 steps
2023-12-22 10:21:23 - Log - INFO: - Interactor 0 finished episode 93 with reward 184.000 in 184 steps
2023-12-22 10:21:29 - Log - INFO: - Interactor 0 finished episode 94 with reward 182.000 in 182 steps
2023-12-22 10:21:31 - Log - INFO: - test_step: 7000, online_eval_reward: 184.400
2023-12-22 10:21:34 - Log - INFO: - Interactor 0 finished episode 95 with reward 194.000 in 194 steps
2023-12-22 10:21:40 - Log - INFO: - Interactor 0 finished episode 96 with reward 185.000 in 185 steps
2023-12-22 10:21:45 - Log - INFO: - Interactor 0 finished episode 97 with reward 166.000 in 166 steps
2023-12-22 10:21:46 - Log - INFO: - test_step: 7500, online_eval_reward: 159.000
2023-12-22 10:21:51 - Log - INFO: - Interactor 0 finished episode 98 with reward 176.000 in 176 steps
2023-12-22 10:21:57 - Log - INFO: - Interactor 0 finished episode 99 with reward 172.000 in 172 steps
2023-12-22 10:21:57 - Log - INFO: - [Trainer.run] Finish training! Time cost: 245.134 s
"""