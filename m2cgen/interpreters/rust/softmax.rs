fn softmax(x: &[f32]) -> Vec<f32> {
    let size: usize = x.len();
    let m: f32 = x.iter().fold(std::f32::MIN, |a, b| a.max(*b));
    let mut exps: Vec<f32> = vec![0.0_f32; size];
    let mut s: f32 = 0.0_f32;
    for (i, &v) in x.iter().enumerate() {
        exps[i] = (v - m).exp();
        s += exps[i];
    }
    exps.iter().map(|&i| i / s).collect::<Vec<f32>>()
}
