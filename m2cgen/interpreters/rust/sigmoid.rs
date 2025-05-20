fn sigmoid(x: f32) -> f32 {
    if x < 0.0_f32 {
        let z: f32 = x.exp();
        return z / (1.0_f32 + z);
    }
    1.0_f32 / (1.0_f32 + (-x).exp())
}
